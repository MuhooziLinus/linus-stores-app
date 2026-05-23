# Linus Stores App - Computer Store Management System

A comprehensive Python-based mobile-friendly web application for managing a computer hardware store.

## Project Structure

```
linus-stores-app/
├── backend/
│   ├── app/
│   │   ├── models/
│   │   ├── routes/
│   │   ├── __init__.py
│   ├── config.py
│   ├── run.py
│   ├── requirements.txt
│   └── .env.example
├── frontend/
│   ├── static/
│   │   ├── css/
│   │   └── js/
│   ├── templates/
│   │   └── index.html
│   └── app.py
├── database/
│   └── schema.sql
└── README.md
```

## Features

### Core Features
- **Product Management**: Add, edit, delete, and search computer hardware products
- **Inventory Management**: Track stock levels, low-stock alerts, and inventory analytics
- **Order Management**: Create orders, manage order status, and order history
- **Customer Management**: Manage customer information and order history
- **Analytics**: Dashboard with sales metrics, top products, and sales by category

### Product Categories
- Processors (CPUs)
- Graphics Cards (GPUs)
- Memory (RAM)
- Storage (SSDs/HDDs)
- Motherboards
- Power Supplies
- Cooling Systems
- Monitors
- Peripherals (Keyboards, Mice, etc.)

## Tech Stack

### Backend
- **Framework**: Flask 2.3.3
- **Database**: MySQL
- **ORM**: Flask-MySQLdb
- **API**: RESTful API with JSON responses

### Frontend
- **HTML5**: Semantic markup
- **CSS3**: Responsive design, Grid, Flexbox
- **JavaScript**: Vanilla JS for API integration
- **Mobile-Responsive**: Works on desktop, tablet, and mobile devices

## Installation

### Prerequisites
- Python 3.8+
- MySQL Server
- pip (Python package manager)

### Backend Setup

1. Navigate to backend directory:
```bash
cd backend
```

2. Create virtual environment:
```bash
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
```

3. Install dependencies:
```bash
pip install -r requirements.txt
```

4. Create `.env` file from `.env.example`:
```bash
cp .env.example .env
```

5. Update `.env` with your MySQL credentials:
```
MYSQL_HOST=localhost
MYSQL_USER=root
MYSQL_PASSWORD=your_password
MYSQL_DB=linus_stores_db
```

6. Initialize database:
```bash
mysql -u root -p < ../database/schema.sql
```

7. Run backend server:
```bash
python run.py
```

Backend will be available at `http://localhost:5000`

### Frontend Setup

1. Navigate to frontend directory:
```bash
cd frontend
```

2. Install dependencies:
```bash
pip install flask flask-cors
```

3. Run frontend server:
```bash
python app.py
```

Frontend will be available at `http://localhost:5001`

## API Endpoints

### Products
- `GET /api/products/` - Get all products
- `GET /api/products/<id>` - Get product by ID
- `GET /api/products/search` - Search products
- `POST /api/products/` - Create product
- `PUT /api/products/<id>` - Update product
- `DELETE /api/products/<id>` - Delete product

### Inventory
- `GET /api/inventory/status` - Get inventory statistics
- `GET /api/inventory/low-stock` - Get low stock items
- `POST /api/inventory/update-stock/<id>` - Update product stock
- `GET /api/inventory/by-category` - Get inventory by category

### Orders
- `GET /api/orders/` - Get all orders
- `GET /api/orders/<id>` - Get order with items
- `POST /api/orders/` - Create new order
- `PUT /api/orders/<id>/status` - Update order status

### Customers
- `GET /api/customers/` - Get all customers
- `GET /api/customers/<id>` - Get customer with orders
- `POST /api/customers/` - Create new customer
- `PUT /api/customers/<id>` - Update customer
- `DELETE /api/customers/<id>` - Delete customer

### Analytics
- `GET /api/analytics/dashboard` - Get dashboard statistics
- `GET /api/analytics/sales-by-category` - Get sales by category
- `GET /api/analytics/top-products` - Get top selling products

## Database Schema

### Tables
- **products**: Store hardware products with pricing and inventory
- **customers**: Customer information
- **orders**: Customer orders
- **order_items**: Individual items in each order

## Usage

1. Open browser and navigate to `http://localhost:5001`
2. View dashboard with key metrics
3. Use sidebar navigation to:
   - Manage products
   - Track inventory
   - Manage orders
   - Manage customers
   - View analytics

## Mobile Responsive
The application is fully responsive and works on:
- Desktop computers
- Tablets
- Mobile phones (with optimized layout)

## Future Enhancements

- [ ] User authentication and authorization
- [ ] Advanced reporting and export features
- [ ] Barcode/QR code scanning
- [ ] Email notifications
- [ ] Payment integration
- [ ] Mobile native apps (iOS/Android)
- [ ] Real-time inventory updates with WebSockets
- [ ] Product images and gallery
- [ ] Reviews and ratings system

## Configuration

All configuration is managed through `.env` file:
- `FLASK_ENV`: development/production
- `FLASK_DEBUG`: Enable/disable debug mode
- `MYSQL_*`: Database connection details
- `SECRET_KEY`: Application secret key

## Troubleshooting

### MySQL Connection Error
- Ensure MySQL server is running
- Check username/password in `.env`
- Verify database exists: `mysql -u root -p linus_stores_db`

### Port Already in Use
- Backend: Change port in `run.py`
- Frontend: Change port in `app.py`

### Missing Dependencies
- Reinstall: `pip install -r requirements.txt`

## License

This project is open source and available under the MIT License.

## Support

For issues or questions, please check the documentation or create an issue in the repository.

---

**Linus Stores App** - Simplified Computer Store Management 
