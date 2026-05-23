from flask import Blueprint, request, jsonify
from flask_mysqldb import MySQL

bp = Blueprint('customers', __name__, url_prefix='/api/customers')
mysql = MySQL()

@bp.route('/', methods=['GET'])
def get_all_customers():
    """Get all customers"""
    try:
        cursor = mysql.get_db().cursor()
        cursor.execute('SELECT * FROM customers')
        customers = cursor.fetchall()
        return jsonify({'success': True, 'data': customers}), 200
    except Exception as e:
        return jsonify({'success': False, 'error': str(e)}), 500

@bp.route('/<int:customer_id>', methods=['GET'])
def get_customer(customer_id):
    """Get single customer with orders"""
    try:
        cursor = mysql.get_db().cursor()
        cursor.execute('SELECT * FROM customers WHERE id = %s', (customer_id,))
        customer = cursor.fetchone()
        
        if not customer:
            return jsonify({'success': False, 'error': 'Customer not found'}), 404
        
        cursor.execute('SELECT * FROM orders WHERE customer_id = %s', (customer_id,))
        orders = cursor.fetchall()
        
        customer['orders'] = orders
        return jsonify({'success': True, 'data': customer}), 200
    except Exception as e:
        return jsonify({'success': False, 'error': str(e)}), 500

@bp.route('/', methods=['POST'])
def create_customer():
    """Create new customer"""
    try:
        data = request.get_json()
        required = ['name', 'email']
        if not all(k in data for k in required):
            return jsonify({'success': False, 'error': 'Missing required fields'}), 400
        
        cursor = mysql.get_db().cursor()
        cursor.execute('''
            INSERT INTO customers (name, email, phone, address)
            VALUES (%s, %s, %s, %s)
        ''', (data['name'], data['email'], data.get('phone', ''), data.get('address', '')))
        mysql.get_db().commit()
        
        return jsonify({'success': True, 'id': cursor.lastrowid}), 201
    except Exception as e:
        return jsonify({'success': False, 'error': str(e)}), 500

@bp.route('/<int:customer_id>', methods=['PUT'])
def update_customer(customer_id):
    """Update customer"""
    try:
        data = request.get_json()
        cursor = mysql.get_db().cursor()
        
        updates = []
        params = []
        for key in ['name', 'email', 'phone', 'address']:
            if key in data:
                updates.append(f'{key} = %s')
                params.append(data[key])
        
        if not updates:
            return jsonify({'success': False, 'error': 'No fields to update'}), 400
        
        params.append(customer_id)
        sql = f'UPDATE customers SET {", ".join(updates)} WHERE id = %s'
        cursor.execute(sql, params)
        mysql.get_db().commit()
        
        return jsonify({'success': True, 'message': 'Customer updated'}), 200
    except Exception as e:
        return jsonify({'success': False, 'error': str(e)}), 500

@bp.route('/<int:customer_id>', methods=['DELETE'])
def delete_customer(customer_id):
    """Delete customer"""
    try:
        cursor = mysql.get_db().cursor()
        cursor.execute('DELETE FROM customers WHERE id = %s', (customer_id,))
        mysql.get_db().commit()
        
        return jsonify({'success': True, 'message': 'Customer deleted'}), 200
    except Exception as e:
        return jsonify({'success': False, 'error': str(e)}), 500
