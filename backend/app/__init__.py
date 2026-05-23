from flask import Flask
from flask_cors import CORS
from flask_mysqldb import MySQL
import os

mysql = MySQL()

def create_app():
    """Application factory"""
    app = Flask(__name__)
    
    # Load configuration
    env = os.getenv('FLASK_ENV', 'development')
    from ..config import config
    app.config.from_object(config[env])
    
    # Initialize extensions
    CORS(app)
    mysql.init_app(app)
    
    # Register blueprints
    from .routes import products, inventory, orders, customers, analytics
    app.register_blueprint(products.bp)
    app.register_blueprint(inventory.bp)
    app.register_blueprint(orders.bp)
    app.register_blueprint(customers.bp)
    app.register_blueprint(analytics.bp)
    
    return app
