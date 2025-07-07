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
- Customers (1) ──── (∞) Orders
- Orders (1) ──── (∞) Order_Items
- Products (1) ──── (∞) Order_Items


## ETL Plan

### Extract
- **Source**: Single CSV file containing approximately 1 million (1,048,576) retail transaction records from the Online Retail II dataset.
- **Tool**: Use pandas to read the CSV data into a DataFrame.
- **Function**: pandas.read_csv() with parse_dates=['InvoiceDate'] to correctly parse dates on load.
- **Options**:
  - Use low_memory=False to avoid dtype guessing issues when reading large files.
- **Inspection**:
  - Perform initial data exploration using df.head(), df.info(), and df.describe() to understand schema, data types, missing values, and data quality issues before transformation.


### Transform
- Placeholder for now

### Load
- Placeholder for now
