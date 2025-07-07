# Retail-Sales-ETL-Pipeline

## Database Schema

This project uses a normalized relational database schema to support analytical queries. Below are the four main tables and their columns:

### Customers
- `customer_id` (INT, Primary Key)
- `country` (TEXT)

### Products
- `product_id` (TEXT, Primary Key)
- `description` (TEXT)
- `unit_price` (FLOAT)

### Orders
- `order_id` (INT, Primary Key)
- `customer_id` (INT, Foreign Key to Customers)
- `order_date` (TIMESTAMP)

### Order_Items
- `order_item_id` (SERIAL/INT, Primary Key)
- `order_id` (INT, Foreign Key to Orders)
- `product_id` (TEXT, Foreign Key to Products)
- `quantity` (INT)
- `unit_price` (FLOAT)
- `line_total` (FLOAT) *(quantity × unit_price)*

### Entity-Relationship Diagram
Customers (1) ──── (∞) Orders
Orders (1) ──── (∞) Order_Items
Products (1) ──── (∞) Order_Items

