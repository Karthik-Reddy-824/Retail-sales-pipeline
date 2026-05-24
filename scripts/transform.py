import pandas as pd

def transform(df):
    # Clean column names
    df.columns = df.columns.str.strip()

    # Convert dates
    df['Order Date'] = pd.to_datetime(df['Order Date'])
    df['Ship Date'] = pd.to_datetime(df['Ship Date'])

    # Create Revenue column
    df['Revenue'] = df['Sales']

    # Remove duplicates
    df = df.drop_duplicates()

    # Create tables
    orders = df[['Order ID', 'Order Date', 'Ship Date', 'Customer ID', 'Product ID', 'Region', 'Revenue']]

    customers = df[['Customer ID', 'Customer Name', 'Segment', 'Region']].drop_duplicates()

    products = df[['Product ID', 'Category', 'Sub-Category', 'Product Name']].drop_duplicates()

    regions = df[['Region', 'State', 'City']].drop_duplicates()

    return orders, customers, products, regions
    
