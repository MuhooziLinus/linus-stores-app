from . import db

class Product:
    """Product model for computer store"""
    
    @staticmethod
    def get_all():
        """Get all products"""
        cursor = db.get_db().cursor()
        cursor.execute('SELECT * FROM products')
        return cursor.fetchall()
    
    @staticmethod
    def get_by_id(product_id):
        """Get product by ID"""
        cursor = db.get_db().cursor()
        cursor.execute('SELECT * FROM products WHERE id = %s', (product_id,))
        return cursor.fetchone()
    
    @staticmethod
    def get_by_category(category):
        """Get products by category"""
        cursor = db.get_db().cursor()
        cursor.execute('SELECT * FROM products WHERE category = %s', (category,))
        return cursor.fetchall()
    
    @staticmethod
    def search(query):
        """Search products by name or description"""
        cursor = db.get_db().cursor()
        search_term = f"%{query}%"
        cursor.execute(
            'SELECT * FROM products WHERE name LIKE %s OR description LIKE %s',
            (search_term, search_term)
        )
        return cursor.fetchall()
    
    @staticmethod
    def create(name, category, price, quantity, description, manufacturer):
        """Create new product"""
        cursor = db.get_db().cursor()
        cursor.execute(
            '''INSERT INTO products (name, category, price, quantity, description, manufacturer)
               VALUES (%s, %s, %s, %s, %s, %s)''',
            (name, category, price, quantity, description, manufacturer)
        )
        db.get_db().commit()
        return cursor.lastrowid
    
    @staticmethod
    def update(product_id, **kwargs):
        """Update product"""
        cursor = db.get_db().cursor()
        updates = ', '.join([f"{key} = %s" for key in kwargs.keys()])
        values = list(kwargs.values()) + [product_id]
        cursor.execute(f'UPDATE products SET {updates} WHERE id = %s', values)
        db.get_db().commit()
    
    @staticmethod
    def delete(product_id):
        """Delete product"""
        cursor = db.get_db().cursor()
        cursor.execute('DELETE FROM products WHERE id = %s', (product_id,))
        db.get_db().commit()
