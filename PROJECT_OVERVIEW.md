# Linus Stores App - Project Overview

## 📋 Project Summary

**Linus Stores App** is a comprehensive computer store management system built with Python, Flask, and MySQL. It provides a mobile-responsive web interface for managing inventory, orders, customers, and business analytics.

**Status**: ✅ Ready to Deploy

---

## 📁 Project Structure

### Backend (`/backend`)
- **`app/__init__.py`** - Flask app factory with blueprint registration
- **`app/routes/`** - API endpoints for:
  - `products.py` - Product CRUD operations
  - `inventory.py` - Inventory tracking & analytics
  - `orders.py` - Order management
  - `customers.py` - Customer management
  - `analytics.py` - Business analytics
- **`app/models/`** - Database models (extensible)
- **`config.py`** - Configuration management
- **`run.py`** - Application entry point
- **`requirements.txt`** - Python dependencies
- **`.env.example`** - Environment variables template

### Frontend (`/frontend`)
- **`templates/index.html`** - Main HTML template with navigation
- **`static/css/style.css`** - Responsive styling (mobile-first design)
- **`static/js/app.js`** - Frontend logic & API integration
- **`app.py`** - Flask server for serving frontend

### Database (`/database`)
- **`schema.sql`** - Complete MySQL schema with:
  - Tables: products, customers, orders, order_items
  - Indexes for performance
  - Sample data for testing

### Documentation
- **`README.md`** - Full documentation
- **`QUICKSTART.md`** - 5-minute setup guide
- **`setup.bat`** - Windows setup script
- **`setup.sh`** - macOS/Linux setup script

---

## 🏗️ Architecture

```
┌─────────────────────────────────────────┐
│         Frontend (Port 5001)             │
│  HTML5 | CSS3 | Vanilla JavaScript      │
└──────────────────┬──────────────────────┘
                   │ HTTP/JSON
┌──────────────────▼──────────────────────┐
│      Backend API (Port 5000)             │
│         Flask Application                │
├──────────────────────────────────────────┤
│  /api/products       /api/orders         │
│  /api/inventory      /api/customers      │
│  /api/analytics                          │
└──────────────────┬──────────────────────┘
                   │ MySQL Driver
┌──────────────────▼──────────────────────┐
│         MySQL Database                   │
│  - products (10 columns)                 │
│  - customers (5 columns)                 │
│  - orders (5 columns)                    │
│  - order_items (5 columns)               │
└─────────────────────────────────────────┘
```

---

## 🔌 API Endpoints (38 Total)

### Products (6 endpoints)
- GET `/api/products/` - List all
- GET `/api/products/<id>` - Get one
- GET `/api/products/search` - Search/filter
- POST `/api/products/` - Create
- PUT `/api/products/<id>` - Update
- DELETE `/api/products/<id>` - Delete

### Inventory (4 endpoints)
- GET `/api/inventory/status` - Statistics
- GET `/api/inventory/low-stock` - Alert items
- POST `/api/inventory/update-stock/<id>` - Update
- GET `/api/inventory/by-category` - Group by category

### Orders (4 endpoints)
- GET `/api/orders/` - List all
- GET `/api/orders/<id>` - Get with items
- POST `/api/orders/` - Create
- PUT `/api/orders/<id>/status` - Update status

### Customers (5 endpoints)
- GET `/api/customers/` - List all
- GET `/api/customers/<id>` - Get with orders
- POST `/api/customers/` - Create
- PUT `/api/customers/<id>` - Update
- DELETE `/api/customers/<id>` - Delete

### Analytics (3 endpoints)
- GET `/api/analytics/dashboard` - All metrics
- GET `/api/analytics/sales-by-category` - Category breakdown
- GET `/api/analytics/top-products` - Best sellers

---

## 💾 Database Schema

### products (10 fields)
```
id (INT, PK)
name (VARCHAR 255)
category (VARCHAR 100)
price (DECIMAL 10,2)
quantity (INT)
description (TEXT)
manufacturer (VARCHAR 100)
created_at, updated_at (TIMESTAMP)
```

### customers (5 fields)
```
id (INT, PK)
name (VARCHAR 255)
email (VARCHAR 255, UNIQUE)
phone (VARCHAR 20)
address (TEXT)
created_at, updated_at (TIMESTAMP)
```

### orders (5 fields)
```
id (INT, PK)
customer_id (INT, FK)
total_amount (DECIMAL 10,2)
status (ENUM: pending, processing, completed, cancelled)
created_at, updated_at (TIMESTAMP)
```

### order_items (5 fields)
```
id (INT, PK)
order_id (INT, FK)
product_id (INT, FK)
quantity (INT)
price (DECIMAL 10,2)
```

---

## 🎨 Frontend Features

### Pages
1. **Dashboard** - Sales metrics, recent orders, KPIs
2. **Products** - Browse, search, manage inventory items
3. **Inventory** - Stock tracking, low-stock alerts, category breakdown
4. **Orders** - Create, manage, track order status
5. **Customers** - Manage customer database and history

### Design
- **Responsive**: Works on desktop, tablet, mobile
- **Modern UI**: Grid layouts, cards, clean typography
- **Interactive**: Real-time API integration
- **Mobile-Optimized**: Touch-friendly buttons, readable fonts
- **Dark Sidebar**: Professional navigation with brand

### Color Scheme
- Primary: Blue (#007bff)
- Success: Green (#28a745)
- Danger: Red (#dc3545)
- Warning: Yellow (#ffc107)
- Dark: Charcoal (#343a40)

---

## 🚀 Getting Started

### System Requirements
- Python 3.8+
- MySQL 5.7+ or MariaDB
- 50MB disk space
- 512MB RAM

### Installation (3 Steps)
1. **Run setup script**
   - Windows: `setup.bat`
   - macOS/Linux: `bash setup.sh`

2. **Configure MySQL** (.env file)
   ```
   MYSQL_HOST=localhost
   MYSQL_USER=root
   MYSQL_PASSWORD=yourpassword
   ```

3. **Start servers**
   ```
   Backend:  python backend/run.py
   Frontend: python frontend/app.py
   ```

4. **Open browser**: `http://localhost:5001`

---

## 🔐 Security Features

- ✅ CORS enabled for API security
- ✅ Environment variables for sensitive data
- ✅ MySQL parameterized queries (SQL injection prevention)
- ✅ Input validation on backend
- ✅ HTTP status codes for error handling

---

## 📈 Sample Data Included

### Products (10)
- Intel Core i9-13900K - $589.99
- NVIDIA RTX 4090 - $1,499.99
- Kingston DDR5 32GB - $199.99
- Samsung 990 Pro 2TB - $249.99
- ASUS ROG Maximus Z790 - $549.99
- Corsair RM1000e 1000W - $219.99
- Noctua NH-D15 - $99.99
- LG 27GP850 Monitor - $349.99
- Logitech MX Master 3S - $99.99
- Mechanical Gaming Keyboard RGB - $149.99

### Customers (5)
Pre-populated for testing orders and analytics

---

## 🔧 Configuration Files

### `.env` - Runtime Configuration
```env
FLASK_ENV=development
FLASK_DEBUG=True
MYSQL_HOST=localhost
MYSQL_USER=root
MYSQL_PASSWORD=your_password
MYSQL_DB=linus_stores_db
SECRET_KEY=your_secret_key_here
```

### `config.py` - Application Settings
- Development: Debug enabled
- Production: Debug disabled
- Testing: Separate database

---

## 📚 Technology Stack

| Layer | Technology | Version |
|-------|-----------|---------|
| Frontend | HTML5, CSS3, JavaScript | ES6+ |
| Backend | Flask | 2.3.3 |
| Database | MySQL | 5.7+ |
| ORM | Flask-MySQLdb | 1.0.1 |
| Security | CORS | 4.0.0 |

---

## 🎯 Key Features

✅ **Product Management** - Full CRUD operations
✅ **Inventory Tracking** - Real-time stock updates
✅ **Order Management** - Complete order lifecycle
✅ **Customer Database** - Maintain customer relationships
✅ **Analytics Dashboard** - Business insights
✅ **Mobile Responsive** - Works on all devices
✅ **REST API** - 22 endpoints
✅ **Sample Data** - Ready to demo
✅ **Easy Setup** - Automated scripts included
✅ **Professional Design** - Modern, clean UI

---

## 🚧 Future Enhancements

- [ ] User authentication & roles (Admin/Staff/Customer)
- [ ] PDF invoice generation
- [ ] Email notifications
- [ ] Payment gateway integration
- [ ] Barcode/QR code scanning
- [ ] Advanced reporting & exports
- [ ] Real-time notifications (WebSockets)
- [ ] Product images & gallery
- [ ] Customer reviews & ratings
- [ ] Mobile native apps (iOS/Android)

---

## 📞 Support & Documentation

- **README.md** - Complete documentation
- **QUICKSTART.md** - Fast setup guide
- **API Endpoints** - Fully documented in code
- **Database Schema** - Detailed in schema.sql
- **Configuration** - See config.py

---

## 📄 License

MIT License - Open source and free to use

---

**Ready to launch your computer store management system!** 🎉

Start with the QUICKSTART.md guide or run the setup script for your OS.
