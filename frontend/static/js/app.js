const API_URL = 'http://localhost:5000/api';

// Load page content
function loadPage(page) {
    const navLinks = document.querySelectorAll('.nav-link');
    navLinks.forEach(link => link.classList.remove('active'));
    event.target.classList.add('active');

    const content = document.getElementById('content');
    content.innerHTML = '<div class="loader"></div>';

    switch(page) {
        case 'dashboard':
            loadDashboard();
            break;
        case 'products':
            loadProducts();
            break;
        case 'inventory':
            loadInventory();
            break;
        case 'orders':
            loadOrders();
            break;
        case 'customers':
            loadCustomers();
            break;
        default:
            loadDashboard();
    }
}

// Dashboard
function loadDashboard() {
    fetch(`${API_URL}/analytics/dashboard`)
        .then(response => response.json())
        .then(data => {
            if (data.success) {
                const stats = data.data;
                let html = `
                    <h2>Dashboard</h2>
                    <div class="dashboard-grid">
                        <div class="card">
                            <div class="card-header">
                                <div>
                                    <div class="card-title">Total Sales</div>
                                    <div class="card-value">$${stats.total_sales.toFixed(2)}</div>
                                </div>
                                <div class="card-icon">💰</div>
                            </div>
                        </div>
                        <div class="card">
                            <div class="card-header">
                                <div>
                                    <div class="card-title">Total Products</div>
                                    <div class="card-value">${stats.total_products}</div>
                                </div>
                                <div class="card-icon">📦</div>
                            </div>
                        </div>
                        <div class="card">
                            <div class="card-header">
                                <div>
                                    <div class="card-title">Total Customers</div>
                                    <div class="card-value">${stats.total_customers}</div>
                                </div>
                                <div class="card-icon">👥</div>
                            </div>
                        </div>
                        <div class="card">
                            <div class="card-header">
                                <div>
                                    <div class="card-title">Total Orders</div>
                                    <div class="card-value">${stats.total_orders}</div>
                                </div>
                                <div class="card-icon">📋</div>
                            </div>
                        </div>
                    </div>

                    <h3 class="mt-20">Recent Orders</h3>
                    <table>
                        <thead>
                            <tr>
                                <th>Order ID</th>
                                <th>Customer</th>
                                <th>Amount</th>
                                <th>Status</th>
                                <th>Date</th>
                            </tr>
                        </thead>
                        <tbody>
                `;
                
                stats.recent_orders.forEach(order => {
                    const date = new Date(order.created_at).toLocaleDateString();
                    html += `
                        <tr>
                            <td>#${order.id}</td>
                            <td>${order.customer_name}</td>
                            <td>$${order.total_amount.toFixed(2)}</td>
                            <td><span class="badge badge-${order.status}">${order.status}</span></td>
                            <td>${date}</td>
                        </tr>
                    `;
                });

                html += `</tbody></table>`;
                document.getElementById('content').innerHTML = html;
            }
        })
        .catch(error => console.error('Error:', error));
}

// Products
function loadProducts() {
    fetch(`${API_URL}/products/`)
        .then(response => response.json())
        .then(data => {
            if (data.success) {
                let html = `
                    <h2>Products</h2>
                    <button class="btn btn-primary mt-20" onclick="openProductModal()">Add New Product</button>
                    <table class="mt-20">
                        <thead>
                            <tr>
                                <th>Product Name</th>
                                <th>Category</th>
                                <th>Price</th>
                                <th>Quantity</th>
                                <th>Manufacturer</th>
                                <th>Actions</th>
                            </tr>
                        </thead>
                        <tbody>
                `;
                
                data.data.forEach(product => {
                    html += `
                        <tr>
                            <td>${product.name}</td>
                            <td>${product.category}</td>
                            <td>$${product.price}</td>
                            <td>${product.quantity}</td>
                            <td>${product.manufacturer}</td>
                            <td>
                                <button class="btn btn-secondary btn-small">Edit</button>
                                <button class="btn btn-danger btn-small">Delete</button>
                            </td>
                        </tr>
                    `;
                });

                html += `</tbody></table>`;
                document.getElementById('content').innerHTML = html;
            }
        })
        .catch(error => console.error('Error:', error));
}

// Inventory
function loadInventory() {
    fetch(`${API_URL}/inventory/status`)
        .then(response => response.json())
        .then(data => {
            if (data.success) {
                const stats = data.data;
                let html = `
                    <h2>Inventory Management</h2>
                    <div class="dashboard-grid">
                        <div class="card">
                            <div class="card-title">Total Products</div>
                            <div class="card-value">${stats.total_products}</div>
                        </div>
                        <div class="card">
                            <div class="card-title">Total Quantity</div>
                            <div class="card-value">${stats.total_quantity}</div>
                        </div>
                        <div class="card">
                            <div class="card-title">Average Price</div>
                            <div class="card-value">$${(stats.avg_price || 0).toFixed(2)}</div>
                        </div>
                    </div>
                `;
                
                document.getElementById('content').innerHTML = html;
                loadLowStockItems();
            }
        })
        .catch(error => console.error('Error:', error));
}

function loadLowStockItems() {
    fetch(`${API_URL}/inventory/low-stock?threshold=10`)
        .then(response => response.json())
        .then(data => {
            if (data.success) {
                let html = `<h3 class="mt-20">Low Stock Items</h3>
                    <table>
                        <thead>
                            <tr>
                                <th>Product Name</th>
                                <th>Current Stock</th>
                                <th>Category</th>
                                <th>Actions</th>
                            </tr>
                        </thead>
                        <tbody>
                `;
                
                data.data.forEach(product => {
                    html += `
                        <tr>
                            <td>${product.name}</td>
                            <td>${product.quantity}</td>
                            <td>${product.category}</td>
                            <td><button class="btn btn-warning btn-small">Reorder</button></td>
                        </tr>
                    `;
                });

                html += `</tbody></table>`;
                document.getElementById('content').innerHTML += html;
            }
        })
        .catch(error => console.error('Error:', error));
}

// Orders
function loadOrders() {
    fetch(`${API_URL}/orders/`)
        .then(response => response.json())
        .then(data => {
            if (data.success) {
                let html = `
                    <h2>Orders</h2>
                    <button class="btn btn-primary mt-20" onclick="openOrderModal()">New Order</button>
                    <table class="mt-20">
                        <thead>
                            <tr>
                                <th>Order ID</th>
                                <th>Total Amount</th>
                                <th>Status</th>
                                <th>Created Date</th>
                                <th>Actions</th>
                            </tr>
                        </thead>
                        <tbody>
                `;
                
                data.data.forEach(order => {
                    const date = new Date(order.created_at).toLocaleDateString();
                    html += `
                        <tr>
                            <td>#${order.id}</td>
                            <td>$${order.total_amount.toFixed(2)}</td>
                            <td><span class="badge badge-${order.status}">${order.status}</span></td>
                            <td>${date}</td>
                            <td><button class="btn btn-secondary btn-small">View</button></td>
                        </tr>
                    `;
                });

                html += `</tbody></table>`;
                document.getElementById('content').innerHTML = html;
            }
        })
        .catch(error => console.error('Error:', error));
}

// Customers
function loadCustomers() {
    fetch(`${API_URL}/customers/`)
        .then(response => response.json())
        .then(data => {
            if (data.success) {
                let html = `
                    <h2>Customers</h2>
                    <button class="btn btn-primary mt-20" onclick="openCustomerModal()">Add New Customer</button>
                    <table class="mt-20">
                        <thead>
                            <tr>
                                <th>Name</th>
                                <th>Email</th>
                                <th>Phone</th>
                                <th>Address</th>
                                <th>Actions</th>
                            </tr>
                        </thead>
                        <tbody>
                `;
                
                data.data.forEach(customer => {
                    html += `
                        <tr>
                            <td>${customer.name}</td>
                            <td>${customer.email}</td>
                            <td>${customer.phone || 'N/A'}</td>
                            <td>${customer.address || 'N/A'}</td>
                            <td>
                                <button class="btn btn-secondary btn-small">Edit</button>
                                <button class="btn btn-danger btn-small">Delete</button>
                            </td>
                        </tr>
                    `;
                });

                html += `</tbody></table>`;
                document.getElementById('content').innerHTML = html;
            }
        })
        .catch(error => console.error('Error:', error));
}

// Modal functions
function openProductModal() {
    alert('Product modal - to be implemented');
}

function openOrderModal() {
    alert('Order modal - to be implemented');
}

function openCustomerModal() {
    alert('Customer modal - to be implemented');
}

// Load dashboard on page load
document.addEventListener('DOMContentLoaded', function() {
    loadDashboard();
});
