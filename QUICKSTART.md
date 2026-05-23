# Linus Stores App - Quick Start Guide

## 🚀 Quick Start (5 minutes)

### Step 1: Set Up MySQL Database

1. Open MySQL client:
```bash
mysql -u root -p
```

2. Run the schema file:
```sql
SOURCE path/to/database/schema.sql;
```

Or from command line:
```bash
mysql -u root -p < database/schema.sql
```

### Step 2: Set Up Backend (Terminal 1)

```bash
cd backend

# Create virtual environment
python -m venv venv

# Activate virtual environment
# On Windows:
venv\Scripts\activate
# On macOS/Linux:
source venv/bin/activate

# Install dependencies
pip install -r requirements.txt

# Create .env file
copy .env.example .env

# Edit .env with your MySQL credentials
# MYSQL_USER=root
# MYSQL_PASSWORD=your_password

# Run backend server
python run.py
```

Server starts at: `http://localhost:5000`

### Step 3: Set Up Frontend (Terminal 2)

```bash
cd frontend

# Install dependencies
pip install flask flask-cors

# Run frontend server
python app.py
```

Frontend opens at: `http://localhost:5001`

## 📊 Default Test Data

The database includes sample data:
- **10 Products**: Computer hardware (CPUs, GPUs, RAM, SSDs, etc.)
- **5 Customers**: Pre-populated for testing
- **0 Orders**: Ready for you to create

## 🔑 Key Features to Test

1. **Dashboard**: View sales metrics and recent orders
2. **Products**: Browse all computer hardware
3. **Inventory**: Check stock levels and low-stock alerts
4. **Orders**: Create and manage orders
5. **Customers**: View and manage customer info
6. **Analytics**: See sales by category and top products

## 🛠️ Configuration

Edit `backend/.env` to change:
- MySQL connection settings
- Flask environment (development/production)
- API port (default: 5000)

## 📱 Mobile Access

Open on your mobile device or tablet:
```
http://your-computer-ip:5001
```

## ⚠️ Troubleshooting

**MySQL Connection Error:**
- Make sure MySQL is running
- Check username/password in `.env`
- Verify database: `mysql -u root -p linus_stores_db`

**Port Already in Use:**
- Edit `run.py` (backend) or `app.py` (frontend) to change ports

**Missing Dependencies:**
- Reinstall: `pip install -r requirements.txt`

## 📚 API Examples

### Get All Products
```bash
curl http://localhost:5000/api/products/
```

### Search Products
```bash
curl "http://localhost:5000/api/products/search?q=GPU"
```

### Get Dashboard Stats
```bash
curl http://localhost:5000/api/analytics/dashboard
```

## 🎯 Next Steps

1. Test the dashboard and existing data
2. Create new products
3. Add customers
4. Create orders and manage them
5. Check analytics for insights

Enjoy using Linus Stores App! 🎉
