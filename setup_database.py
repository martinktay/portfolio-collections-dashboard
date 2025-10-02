#!/usr/bin/env python3
"""
Setup script to create SQLite database from CSV files
"""
import sqlite3
import pandas as pd
import os

# Database path
DB_PATH = 'data/water_collections_demo.sqlite'

# CSV files to import
CSV_FILES = {
    'customers': 'data/customers.csv',
    'bills': 'data/bills.csv', 
    'payments': 'data/payments.csv',
    'collections_actions': 'data/collections_actions.csv'
}

def create_database():
    """Create SQLite database and import CSV data"""
    
    # Remove existing database if it exists
    if os.path.exists(DB_PATH):
        os.remove(DB_PATH)
        print(f"Removed existing database: {DB_PATH}")
    
    # Create connection
    con = sqlite3.connect(DB_PATH)
    print(f"Created database: {DB_PATH}")
    
    try:
        # Import each CSV file
        for table_name, csv_path in CSV_FILES.items():
            if os.path.exists(csv_path):
                df = pd.read_csv(csv_path)
                df.to_sql(table_name, con, index=False, if_exists='replace')
                print(f"Imported {len(df)} rows into {table_name} table")
            else:
                print(f"Warning: {csv_path} not found")
        
        # Verify data integrity
        print("\nData verification:")
        for table_name in CSV_FILES.keys():
            count = pd.read_sql(f'SELECT COUNT(*) as count FROM {table_name}', con).iloc[0, 0]
            print(f"{table_name}: {count} rows")
        
        # Check referential integrity
        customers_count = pd.read_sql('SELECT COUNT(DISTINCT customer_id) as count FROM customers', con).iloc[0, 0]
        bills_customers = pd.read_sql('SELECT COUNT(DISTINCT customer_id) as count FROM bills', con).iloc[0, 0]
        payments_customers = pd.read_sql('SELECT COUNT(DISTINCT customer_id) as count FROM payments', con).iloc[0, 0]
        actions_customers = pd.read_sql('SELECT COUNT(DISTINCT customer_id) as count FROM collections_actions', con).iloc[0, 0]
        
        print(f"\nReferential integrity check:")
        print(f"Unique customers in customers table: {customers_count}")
        print(f"Unique customers in bills table: {bills_customers}")
        print(f"Unique customers in payments table: {payments_customers}")
        print(f"Unique customers in collections_actions table: {actions_customers}")
        
    finally:
        con.close()
        print(f"\nDatabase setup complete!")

if __name__ == "__main__":
    create_database()