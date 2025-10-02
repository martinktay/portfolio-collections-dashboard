#!/usr/bin/env python3
"""
Create KPI calculation views for default rate analysis
"""
import sqlite3
import pandas as pd

DB_PATH = 'data/water_collections_demo.sqlite'

def create_kpi_views():
    """Create analytical views for KPI calculations"""
    
    con = sqlite3.connect(DB_PATH)
    
    try:
        with con:
            print("Creating KPI calculation views...")
            
            # Drop existing view if it exists
            con.execute('DROP VIEW IF EXISTS bill_targets')
            
            # Create bill_targets view with default rate logic
            # D-3 to D+60 payment window (3 days before due date to 60 days after)
            bill_targets_sql = """
            CREATE VIEW bill_targets AS
            SELECT 
                b.customer_id,
                b.bill_period_end,
                b.due_date,
                b.bill_amount,
                b.usage_m3,
                COALESCE((
                    SELECT SUM(p.amount) 
                    FROM payments p 
                    WHERE p.customer_id = b.customer_id 
                    AND DATE(p.payment_date) > DATE(b.due_date, '-3 day')
                    AND DATE(p.payment_date) <= DATE(b.due_date, '+60 day')
                ), 0.0) AS paid_in_window,
                CASE 
                    WHEN COALESCE((
                        SELECT SUM(p2.amount) 
                        FROM payments p2 
                        WHERE p2.customer_id = b.customer_id 
                        AND DATE(p2.payment_date) > DATE(b.due_date, '-3 day')
                        AND DATE(p2.payment_date) <= DATE(b.due_date, '+60 day')
                    ), 0.0) >= b.bill_amount - 1.0 
                    THEN 0 
                    ELSE 1 
                END AS default_60d
            FROM bills b
            """
            
            con.execute(bill_targets_sql)
            print("✓ Created bill_targets view with default rate calculation")
            
            # Test the view
            test_query = """
            SELECT 
                COUNT(*) as total_bills,
                SUM(default_60d) as defaults,
                ROUND(AVG(default_60d), 4) as default_rate,
                ROUND(AVG(bill_amount), 2) as avg_bill_amount,
                ROUND(AVG(paid_in_window), 2) as avg_paid
            FROM bill_targets
            """
            
            result = pd.read_sql(test_query, con)
            print(f"\nView validation:")
            print(f"Total bills: {result.iloc[0]['total_bills']:,}")
            print(f"Default events: {result.iloc[0]['defaults']:,}")
            print(f"Overall default rate: {result.iloc[0]['default_rate']:.1%}")
            print(f"Average bill amount: £{result.iloc[0]['avg_bill_amount']}")
            print(f"Average paid in window: £{result.iloc[0]['avg_paid']}")
            
            # Test monthly aggregation
            monthly_test = pd.read_sql("""
            SELECT 
                strftime('%Y-%m', bill_period_end) AS month,
                COUNT(*) as bills,
                ROUND(AVG(default_60d), 4) as default_rate
            FROM bill_targets 
            GROUP BY 1 
            ORDER BY 1 
            LIMIT 5
            """, con)
            
            print(f"\nSample monthly data:")
            print(monthly_test.to_string(index=False))
            
    finally:
        con.close()
        print(f"\nKPI views created successfully!")

if __name__ == "__main__":
    create_kpi_views()