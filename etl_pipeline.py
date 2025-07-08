"""Load Online Retail II CSV data into pandas DataFrame."""

import pandas as pd
import logging
from sqlalchemy import create_engine

# logging setup
logging.basicConfig(level=logging.INFO)

# Extract Step
def extract_data(filepath):

    logging.info(f"Reading data from {filepath}")

    # Reads a large CSV file into a pandas DataFrame.
    df = pd.read_csv(
        filepath,
        parse_dates=['InvoiceDate'],  # Converts the InvoiceDate column to datetime.
        low_memory=False              # Handles large files safely.
    )

    logging.info(f"Finished reading data. Shape: {df.shape}")
    return df


# Transform Step

def transform_data(raw_data):
    """
    - Cleans raw data.
    - Splits into Customers, Products, Orders, and Order_Items DataFrames.
    """
    df = raw_data.copy()

    # Drop rows with missing Customer ID
    df = df.dropna(subset=['Customer ID'])

    # Convert Customer ID to integer
    df['Customer ID'] = df['Customer ID'].astype(int)

    # Compute line_total
    df['line_total'] = df['Quantity'] * df['Price']

    # Customers table
    customers = df[['Customer ID', 'Country']].drop_duplicates().reset_index(drop=True)

    # Products table
    products = df[['StockCode', 'Description', 'Price']].drop_duplicates().reset_index(drop=True)

    # Orders table
    orders = df[['Invoice', 'Customer ID', 'InvoiceDate']].drop_duplicates().reset_index(drop=True)

    # Order_Items table
    order_items = df[['Invoice', 'StockCode', 'Quantity', 'Price', 'line_total']].reset_index(drop=True)

    return customers, products, orders, order_items


# Load

def load_data(customers, products, orders, order_items):
    """
    Load Step:
    - Saves cleaned DataFrames to a MySQL database.
    - Each DataFrame becomes its own table.
    """
    # Replace with your actual credentials
    username = 'root'
    password = 'pass'
    host = 'localhost'
    port = '3306'
    database = 'retail_db'

    connection_string = f'mysql+mysqlconnector://{username}:{password}@{host}:{port}/{database}'
    engine = create_engine(connection_string)

    customers.to_sql('customers', con=engine, if_exists='replace', index=False)
    products.to_sql('products', con=engine, if_exists='replace', index=False)
    orders.to_sql('orders', con=engine, if_exists='replace', index=False)
    order_items.to_sql('order_items', con=engine, if_exists='replace', index=False)

    print(f"\n Data successfully loaded into MySQL database: {database}")



if __name__ == "__main__":
    # file path
    csv_path = '/Users/joonvang/Desktop/DE Project/Project #1/online_retail_II.csv'
    
    # Extract step
    data = extract_data(csv_path)
    
    print(data.head())
    print(data.info())

    # Transform step
    customers, products, orders, order_items = transform_data(data)

    print("\nCustomers Table:")
    print(customers.head())

    print("\nProducts Table:")
    print(products.head())

    print("\nOrders Table:")
    print(orders.head())

    print("\nOrder Items Table:")
    print(order_items.head())

    # Load step
    load_data(customers, products, orders, order_items)
