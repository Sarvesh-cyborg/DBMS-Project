-- Create the database
CREATE DATABASE grocery_management_db;
USE grocery_management_db;

-- Product Table
CREATE TABLE product (
    product_id INT PRIMARY KEY AUTO_INCREMENT,
    name VARCHAR(100) NOT NULL,
    category VARCHAR(50),
    price DECIMAL(10,2) NOT NULL,
    stock_quantity INT NOT NULL,
    expiry_date DATE
);

-- Customer Table
CREATE TABLE customer (
    customer_id INT PRIMARY KEY AUTO_INCREMENT,
    name VARCHAR(100) NOT NULL,
    phone VARCHAR(15) UNIQUE NOT NULL,
    email VARCHAR(100) UNIQUE
);

-- Orders Table
CREATE TABLE order_info (
    order_id INT PRIMARY KEY AUTO_INCREMENT,
    customer_id INT,
    order_date TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    total_price DECIMAL(10,2) DEFAULT 0,
    FOREIGN KEY (customer_id) REFERENCES customer(customer_id) ON DELETE SET NULL
);

-- Order Details Table (Many-to-Many between Orders and Products)
CREATE TABLE order_details (
    order_detail_id INT PRIMARY KEY AUTO_INCREMENT,
    order_id INT,
    product_id INT,
    quantity INT NOT NULL,
    price DECIMAL(10,2) NOT NULL,
    FOREIGN KEY (order_id) REFERENCES order_info(order_id) ON DELETE CASCADE,
    FOREIGN KEY (product_id) REFERENCES product(product_id) ON DELETE CASCADE
);

-- Insert Sample Data
INSERT INTO product (name, category, price, stock_quantity, expiry_date) 
VALUES 
('Milk', 'Dairy', 2.50, 50, '2025-06-01'),
('Bread', 'Bakery', 1.20, 30, '2025-02-28'),
('Apple', 'Fruits', 0.80, 100, '2025-03-15');

INSERT INTO customer (name, phone, email) 
VALUES 
('John Doe', '1234567890', 'john@example.com'),
('Jane Smith', '0987654321', 'jane@example.com');

INSERT INTO order_info (customer_id, total_price) VALUES (1, 5.00);
INSERT INTO order_details (order_id, product_id, quantity, price) VALUES (1, 1, 2, 5.00);

show Tables;
use grocery_management_db;