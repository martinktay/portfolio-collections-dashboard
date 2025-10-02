#!/usr/bin/env python3
"""
Create database indexes for performance optimisation
"""
import sqlite3

DB_PATH = 'data/water_collections_demo.sqlite'

def create_indexes():
    """Create composite indexes for analytical queries"""
    
    con = sqlite3.connect(DB_PATH)
    
    try:
        with con:
            # Create indexes for efficient joins and date-based queries
            print("Creating database indexes...")
            
            # Bills table indexes
            con.execute('CREATE INDEX IF NOT EXISTS ix_bills_cid_date ON bills(customer_id, bill_period_end)')
            print("✓ Created index on bills(customer_id, bill_period_end)")
            
            con.execute('CREATE INDEX IF NOT EXISTS ix_bills_due_date ON bills(due_date)')
            print("✓ Created index on bills(due_date)")
            
            # Payments table indexes  
            con.execute('CREATE INDEX IF NOT EXISTS ix_payments_cid_date ON payments(customer_id, payment_date)')
            print("✓ Created index on payments(customer_id, payment_date)")
            
            con.execute('CREATE INDEX IF NOT EXISTS ix_payments_date ON payments(payment_date)')
            print("✓ Created index on payments(payment_date)")
            
            # Collections actions table indexes
            con.execute('CREATE INDEX IF NOT EXISTS ix_actions_cid_date ON collections_actions(customer_id, action_date)')
            print("✓ Created index on collections_actions(customer_id, action_date)")
            
            con.execute('CREATE INDEX IF NOT EXISTS ix_actions_date ON collections_actions(action_date)')
            print("✓ Created index on collections_actions(action_date)")
            
            # Customer table index (already has primary key, but add for joins)
            con.execute('CREATE INDEX IF NOT EXISTS ix_customers_region ON customers(region)')
            print("✓ Created index on customers(region)")
            
            con.execute('CREATE INDEX IF NOT EXISTS ix_customers_income ON customers(income_band)')
            print("✓ Created index on customers(income_band)")
            
        print("\nAll indexes created successfully!")
        
        # Verify indexes were created
        indexes = con.execute("SELECT name FROM sqlite_master WHERE type='index' AND name LIKE 'ix_%'").fetchall()
        print(f"\nCreated {len(indexes)} custom indexes:")
        for idx in indexes:
            print(f"  - {idx[0]}")
            
    finally:
        con.close()

if __name__ == "__main__":
    create_indexes()