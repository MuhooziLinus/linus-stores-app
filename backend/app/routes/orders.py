from flask import Blueprint, request, jsonify
from flask_mysqldb import MySQL
from datetime import datetime

bp = Blueprint('orders', __name__, url_prefix='/api/orders')
mysql = MySQL()

@bp.route('/', methods=['GET'])
def get_all_orders():
    """Get all orders"""
    try:
        cursor = mysql.get_db().cursor()
        cursor.execute('SELECT * FROM orders ORDER BY created_at DESC')
        orders = cursor.fetchall()
        return jsonify({'success': True, 'data': orders}), 200
    except Exception as e:
        return jsonify({'success': False, 'error': str(e)}), 500

@bp.route('/<int:order_id>', methods=['GET'])
def get_order(order_id):
    """Get single order with items"""
    try:
        cursor = mysql.get_db().cursor()
        cursor.execute('SELECT * FROM orders WHERE id = %s', (order_id,))
        order = cursor.fetchone()
        
        if not order:
            return jsonify({'success': False, 'error': 'Order not found'}), 404
        
        cursor.execute('''
            SELECT oi.*, p.name, p.price
            FROM order_items oi
            JOIN products p ON oi.product_id = p.id
            WHERE oi.order_id = %s
        ''', (order_id,))
        items = cursor.fetchall()
        
        order['items'] = items
        return jsonify({'success': True, 'data': order}), 200
    except Exception as e:
        return jsonify({'success': False, 'error': str(e)}), 500

@bp.route('/', methods=['POST'])
def create_order():
    """Create new order"""
    try:
        data = request.get_json()
        customer_id = data.get('customer_id')
        items = data.get('items', [])
        
        if not customer_id or not items:
            return jsonify({'success': False, 'error': 'Customer ID and items required'}), 400
        
        cursor = mysql.get_db().cursor()
        total_amount = 0
        
        # Calculate total amount
        for item in items:
            cursor.execute('SELECT price FROM products WHERE id = %s', (item['product_id'],))
            product = cursor.fetchone()
            if product:
                total_amount += product['price'] * item['quantity']
        
        # Create order
        cursor.execute('''
            INSERT INTO orders (customer_id, total_amount, status, created_at)
            VALUES (%s, %s, %s, %s)
        ''', (customer_id, total_amount, 'pending', datetime.now()))
        mysql.get_db().commit()
        order_id = cursor.lastrowid
        
        # Add order items
        for item in items:
            cursor.execute('''
                INSERT INTO order_items (order_id, product_id, quantity, price)
                VALUES (%s, %s, %s, (SELECT price FROM products WHERE id = %s))
            ''', (order_id, item['product_id'], item['quantity'], item['product_id']))
            
            # Update product quantity
            cursor.execute('''
                UPDATE products SET quantity = quantity - %s WHERE id = %s
            ''', (item['quantity'], item['product_id']))
        
        mysql.get_db().commit()
        return jsonify({'success': True, 'id': order_id}), 201
    except Exception as e:
        return jsonify({'success': False, 'error': str(e)}), 500

@bp.route('/<int:order_id>/status', methods=['PUT'])
def update_order_status(order_id):
    """Update order status"""
    try:
        data = request.get_json()
        status = data.get('status')
        
        if not status:
            return jsonify({'success': False, 'error': 'Status required'}), 400
        
        cursor = mysql.get_db().cursor()
        cursor.execute('UPDATE orders SET status = %s WHERE id = %s', (status, order_id))
        mysql.get_db().commit()
        
        return jsonify({'success': True, 'message': 'Order status updated'}), 200
    except Exception as e:
        return jsonify({'success': False, 'error': str(e)}), 500
