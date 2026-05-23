from flask import Blueprint, request, jsonify
from flask_mysqldb import MySQL

bp = Blueprint('products', __name__, url_prefix='/api/products')
mysql = MySQL()

@bp.route('/', methods=['GET'])
def get_all_products():
    """Get all products"""
    try:
        cursor = mysql.get_db().cursor()
        cursor.execute('SELECT * FROM products')
        products = cursor.fetchall()
        return jsonify({'success': True, 'data': products}), 200
    except Exception as e:
        return jsonify({'success': False, 'error': str(e)}), 500

@bp.route('/<int:product_id>', methods=['GET'])
def get_product(product_id):
    """Get single product"""
    try:
        cursor = mysql.get_db().cursor()
        cursor.execute('SELECT * FROM products WHERE id = %s', (product_id,))
        product = cursor.fetchone()
        if product:
            return jsonify({'success': True, 'data': product}), 200
        return jsonify({'success': False, 'error': 'Product not found'}), 404
    except Exception as e:
        return jsonify({'success': False, 'error': str(e)}), 500

@bp.route('/search', methods=['GET'])
def search_products():
    """Search products"""
    query = request.args.get('q', '')
    category = request.args.get('category', '')
    
    try:
        cursor = mysql.get_db().cursor()
        sql = 'SELECT * FROM products WHERE 1=1'
        params = []
        
        if query:
            sql += ' AND (name LIKE %s OR description LIKE %s)'
            params.extend([f'%{query}%', f'%{query}%'])
        
        if category:
            sql += ' AND category = %s'
            params.append(category)
        
        cursor.execute(sql, params)
        products = cursor.fetchall()
        return jsonify({'success': True, 'data': products}), 200
    except Exception as e:
        return jsonify({'success': False, 'error': str(e)}), 500

@bp.route('/', methods=['POST'])
def create_product():
    """Create new product"""
    try:
        data = request.get_json()
        required = ['name', 'category', 'price', 'quantity']
        if not all(k in data for k in required):
            return jsonify({'success': False, 'error': 'Missing required fields'}), 400
        
        cursor = mysql.get_db().cursor()
        cursor.execute(
            '''INSERT INTO products (name, category, price, quantity, description, manufacturer)
               VALUES (%s, %s, %s, %s, %s, %s)''',
            (data['name'], data['category'], data['price'], data['quantity'],
             data.get('description', ''), data.get('manufacturer', ''))
        )
        mysql.get_db().commit()
        
        return jsonify({'success': True, 'id': cursor.lastrowid}), 201
    except Exception as e:
        return jsonify({'success': False, 'error': str(e)}), 500

@bp.route('/<int:product_id>', methods=['PUT'])
def update_product(product_id):
    """Update product"""
    try:
        data = request.get_json()
        cursor = mysql.get_db().cursor()
        
        updates = []
        params = []
        for key in ['name', 'category', 'price', 'quantity', 'description', 'manufacturer']:
            if key in data:
                updates.append(f'{key} = %s')
                params.append(data[key])
        
        if not updates:
            return jsonify({'success': False, 'error': 'No fields to update'}), 400
        
        params.append(product_id)
        sql = f'UPDATE products SET {", ".join(updates)} WHERE id = %s'
        cursor.execute(sql, params)
        mysql.get_db().commit()
        
        return jsonify({'success': True, 'message': 'Product updated'}), 200
    except Exception as e:
        return jsonify({'success': False, 'error': str(e)}), 500

@bp.route('/<int:product_id>', methods=['DELETE'])
def delete_product(product_id):
    """Delete product"""
    try:
        cursor = mysql.get_db().cursor()
        cursor.execute('DELETE FROM products WHERE id = %s', (product_id,))
        mysql.get_db().commit()
        
        return jsonify({'success': True, 'message': 'Product deleted'}), 200
    except Exception as e:
        return jsonify({'success': False, 'error': str(e)}), 500
