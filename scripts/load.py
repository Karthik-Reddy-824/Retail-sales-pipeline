import sqlite3
import os
def load(orders, customers, products, regions, db_path="db/sales.db"):
    # Ensure db directory exists
    os.makedirs(os.path.dirname(db_path) or '.', exist_ok=True)
    
    conn = sqlite3.connect(db_path)
    
    try:
        orders.to_sql('orders', conn, if_exists='replace', index=False)
        customers.to_sql('customers', conn, if_exists='replace', index=False)
        products.to_sql('products', conn, if_exists='replace', index=False)
        regions.to_sql('regions', conn, if_exists='replace', index=False)
        
        conn.commit()
        print(f"Data successfully loaded to {db_path}")
    except Exception as e:
        conn.rollback()
        print(f"Error loading data: {e}")
        raise
    finally:
        conn.close()