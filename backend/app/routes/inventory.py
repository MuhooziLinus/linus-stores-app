from flask import Blueprint, request, jsonify
from flask_mysqldb import MySQL

bp = Blueprint('inventory', __name__, url_prefix='/api/inventory')
mysql = MySQL()

@bp.route('/status', methods=['GET'])
def inventory_status():
    """Get inventory status"""
    try:
        cursor = mysql.get_db().cursor()
        cursor.execute('''
            SELECT 
                COUNT(*) as total_products,
                SUM(quantity) as total_quantity,
                AVG(price) as avg_price
            FROM products
        ''')
        result = cursor.fetchone()
        return jsonify({'success': True, 'data': result}), 200
    except Exception as e:
        return jsonify({'success': False, 'error': str(e)}), 500

@bp.route('/low-stock', methods=['GET'])
def low_stock():
    """Get products with low stock"""
    threshold = request.args.get('threshold', 10, type=int)
    
    try:
        cursor = mysql.get_db().cursor()
        cursor.execute(
            'SELECT * FROM products WHERE quantity <= %s ORDER BY quantity ASC',
            (threshold,)
        )
        products = cursor.fetchall()
        return jsonify({'success': True, 'data': products}), 200
    except Exception as e:
        return jsonify({'success': False, 'error': str(e)}), 500

@bp.route('/update-stock/<int:product_id>', methods=['POST'])
def update_stock(product_id):
    """Update product stock"""
    try:
        data = request.get_json()
        quantity = data.get('quantity')
        
        if quantity is None:
            return jsonify({'success': False, 'error': 'Quantity required'}), 400
        
        cursor = mysql.get_db().cursor()
        cursor.execute('UPDATE products SET quantity = %s WHERE id = %s', 
                      (quantity, product_id))
        mysql.get_db().commit()
        
        return jsonify({'success': True, 'message': 'Stock updated'}), 200
    except Exception as e:
        return jsonify({'success': False, 'error': str(e)}), 500

@bp.route('/by-category', methods=['GET'])
def inventory_by_category():
    """Get inventory grouped by category"""
    try:
        cursor = mysql.get_db().cursor()
        cursor.execute('''
            SELECT category, COUNT(*) as product_count, SUM(quantity) as total_quantity
            FROM products
            GROUP BY category
        ''')
        result = cursor.fetchall()
        return jsonify({'success': True, 'data': result}), 200
    except Exception as e:
        return jsonify({'success': False, 'error': str(e)}), 500
