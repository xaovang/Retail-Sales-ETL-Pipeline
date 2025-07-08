# Online-Retail-Sales-ETL-Pipeline

This project demonstrates an end-to-end ETL (Extract, Transform, Load) pipeline for the **Online Retail II** dataset.

**Goal:**  
Convert messy raw sales transaction data into a **clean, normalized relational schema** suitable for analysis and reporting.

---

## Features
- Reads large CSV (~1 million rows) with pandas.
- Cleans and transforms raw sales data into 4 normalized tables.
- Loads data into a MySQL database using SQLAlchemy.
- Production-style code with logging and modular ETL functions.

---

## Dataset
**Source:** [UCI Online Retail II] (https://www.kaggle.com/datasets/mashlyn/online-retail-ii-uci?resource=download)

**Fields in CSV:**  
- Invoice
- StockCode
- Description
- Quantity
- InvoiceDate
- Price
- Customer ID
- Country

## Python Code File Name
- etl_pipeline.py


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
- **Source**: Single CSV file containing over 1 million retail transaction records from the Online Retail II dataset.
- **Tool**: Use pandas to read the CSV data into a DataFrame.
- **Function**: pandas.read_csv() with parse_dates=['InvoiceDate'] to correctly parse dates on load.
- **Options**:
  - Use low_memory=False to avoid dtype guessing issues when reading large files.
- **Inspection**:
  - Perform initial data exploration using df.head(), df.info(), and df.describe() to understand schema, data types, missing values, and data quality issues before transformation.


### Transform

- Drop rows with missing Customer ID.
- Ensure Customer ID is integer type.
- Remove duplicates in Customers and Products tables.
- Compute line_total = Quantity * Price for Order_Items.
- Split cleaned data into four separate DataFrames:
  - Customers
  - Products
  - Orders
  - Order_Items

### Load
- Loads cleaned data into MySQL database named `retail_db`.
- Creates four normalized tables:
  - customers
  - products
  - orders
  - order_items
- Uses SQLAlchemy and mysql-connector to connect and write data.
