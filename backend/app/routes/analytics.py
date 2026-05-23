from flask import Blueprint, request, jsonify
from flask_mysqldb import MySQL

bp = Blueprint('analytics', __name__, url_prefix='/api/analytics')
mysql = MySQL()

@bp.route('/dashboard', methods=['GET'])
def dashboard():
    """Get dashboard analytics"""
    try:
        cursor = mysql.get_db().cursor()
        
        # Total sales
        cursor.execute('SELECT SUM(total_amount) as total_sales FROM orders WHERE status = "completed"')
        total_sales = cursor.fetchone()
        
        # Total products
        cursor.execute('SELECT COUNT(*) as total_products FROM products')
        total_products = cursor.fetchone()
        
        # Total customers
        cursor.execute('SELECT COUNT(*) as total_customers FROM customers')
        total_customers = cursor.fetchone()
        
        # Total orders
        cursor.execute('SELECT COUNT(*) as total_orders FROM orders')
        total_orders = cursor.fetchone()
        
        # Recent orders
        cursor.execute('''
            SELECT o.*, c.name as customer_name
            FROM orders o
            JOIN customers c ON o.customer_id = c.id
            ORDER BY o.created_at DESC LIMIT 5
        ''')
        recent_orders = cursor.fetchall()
        
        data = {
            'total_sales': total_sales['total_sales'] or 0,
            'total_products': total_products['total_products'],
            'total_customers': total_customers['total_customers'],
            'total_orders': total_orders['total_orders'],
            'recent_orders': recent_orders
        }
        
        return jsonify({'success': True, 'data': data}), 200
    except Exception as e:
        return jsonify({'success': False, 'error': str(e)}), 500

@bp.route('/sales-by-category', methods=['GET'])
def sales_by_category():
    """Get sales grouped by category"""
    try:
        cursor = mysql.get_db().cursor()
        cursor.execute('''
            SELECT p.category, COUNT(oi.id) as items_sold, SUM(oi.price * oi.quantity) as revenue
            FROM order_items oi
            JOIN products p ON oi.product_id = p.id
            GROUP BY p.category
        ''')
        result = cursor.fetchall()
        return jsonify({'success': True, 'data': result}), 200
    except Exception as e:
        return jsonify({'success': False, 'error': str(e)}), 500

@bp.route('/top-products', methods=['GET'])
def top_products():
    """Get top selling products"""
    limit = request.args.get('limit', 10, type=int)
    
    try:
        cursor = mysql.get_db().cursor()
        cursor.execute('''
            SELECT p.id, p.name, COUNT(oi.id) as times_sold, SUM(oi.quantity) as total_quantity
            FROM order_items oi
            JOIN products p ON oi.product_id = p.id
            GROUP BY p.id, p.name
            ORDER BY total_quantity DESC LIMIT %s
        ''', (limit,))
        result = cursor.fetchall()
        return jsonify({'success': True, 'data': result}), 200
    except Exception as e:
        return jsonify({'success': False, 'error': str(e)}), 500
