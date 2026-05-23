-- Linus Stores App Database Schema
-- Computer Store Management System

CREATE DATABASE IF NOT EXISTS linus_stores_db;
USE linus_stores_db;

-- Products table
CREATE TABLE IF NOT EXISTS products (
    id INT AUTO_INCREMENT PRIMARY KEY,
    name VARCHAR(255) NOT NULL,
    category VARCHAR(100) NOT NULL,
    price DECIMAL(10, 2) NOT NULL,
    quantity INT NOT NULL DEFAULT 0,
    description TEXT,
    manufacturer VARCHAR(100),
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
    INDEX idx_category (category),
    INDEX idx_name (name)
);

-- Customers table
CREATE TABLE IF NOT EXISTS customers (
    id INT AUTO_INCREMENT PRIMARY KEY,
    name VARCHAR(255) NOT NULL,
    email VARCHAR(255) UNIQUE NOT NULL,
    phone VARCHAR(20),
    address TEXT,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
    INDEX idx_email (email),
    INDEX idx_name (name)
);

-- Orders table
CREATE TABLE IF NOT EXISTS orders (
    id INT AUTO_INCREMENT PRIMARY KEY,
    customer_id INT NOT NULL,
    total_amount DECIMAL(10, 2) NOT NULL,
    status ENUM('pending', 'processing', 'completed', 'cancelled') DEFAULT 'pending',
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
    FOREIGN KEY (customer_id) REFERENCES customers(id),
    INDEX idx_customer_id (customer_id),
    INDEX idx_status (status),
    INDEX idx_created_at (created_at)
);

-- Order Items table
CREATE TABLE IF NOT EXISTS order_items (
    id INT AUTO_INCREMENT PRIMARY KEY,
    order_id INT NOT NULL,
    product_id INT NOT NULL,
    quantity INT NOT NULL,
    price DECIMAL(10, 2) NOT NULL,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    FOREIGN KEY (order_id) REFERENCES orders(id),
    FOREIGN KEY (product_id) REFERENCES products(id),
    INDEX idx_order_id (order_id),
    INDEX idx_product_id (product_id)
);

-- Sample Data
INSERT INTO products (name, category, price, quantity, description, manufacturer) VALUES
('Intel Core i9-13900K', 'Processors', 589.99, 15, 'High-performance desktop processor', 'Intel'),
('NVIDIA RTX 4090', 'Graphics Cards', 1499.99, 8, 'Premium graphics card for gaming and workstations', 'NVIDIA'),
('Kingston DDR5 32GB', 'RAM', 199.99, 25, '32GB DDR5 memory module', 'Kingston'),
('Samsung 990 Pro 2TB', 'Storage', 249.99, 20, '2TB NVMe SSD', 'Samsung'),
('ASUS ROG Maximus Z790', 'Motherboards', 549.99, 12, 'Premium Z790 motherboard', 'ASUS'),
('Corsair RM1000e 1000W', 'Power Supplies', 219.99, 18, '1000W modular power supply', 'Corsair'),
('Noctua NH-D15', 'Cooling', 99.99, 30, 'Premium air CPU cooler', 'Noctua'),
('LG 27GP850 Monitor', 'Monitors', 349.99, 10, '27" IPS gaming monitor', 'LG'),
('Logitech MX Master 3S', 'Peripherals', 99.99, 35, 'Professional wireless mouse', 'Logitech'),
('Mechanical Gaming Keyboard RGB', 'Peripherals', 149.99, 22, 'RGB mechanical keyboard', 'Generic');

INSERT INTO customers (name, email, phone, address) VALUES
('John Smith', 'john.smith@email.com', '555-0101', '123 Main St, City, State'),
('Sarah Johnson', 'sarah.johnson@email.com', '555-0102', '456 Oak Ave, City, State'),
('Michael Brown', 'michael.brown@email.com', '555-0103', '789 Pine Rd, City, State'),
('Emily Davis', 'emily.davis@email.com', '555-0104', '321 Elm St, City, State'),
('David Wilson', 'david.wilson@email.com', '555-0105', '654 Maple Dr, City, State');
