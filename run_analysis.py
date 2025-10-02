#!/usr/bin/env python3
"""
Run the portfolio collections analysis and generate figures
"""
import os
import sqlite3
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

# Database connection
DB_PATH = 'data/water_collections_demo.sqlite'
con = sqlite3.connect(DB_PATH)

print("🚀 Running Portfolio Collections Dashboard Analysis...")

try:
    # Set up plotting style
    sns.set_theme(style="whitegrid")
    plt.rcParams['figure.dpi'] = 100
    plt.rcParams['savefig.dpi'] = 200
    
    # Ensure output directory exists
    os.makedirs('outputs/figures', exist_ok=True)
    
    # Load data for analysis
    print("📊 Loading data...")
    
    # Monthly trend analysis
    kpi_monthly = pd.read_sql("""
    SELECT 
        strftime('%Y-%m', bill_period_end) AS month,
        AVG(default_60d) AS default_rate,
        SUM(bill_amount) AS billed,
        SUM(paid_in_window) AS paid,
        COUNT(*) as bill_count
    FROM bill_targets 
    GROUP BY 1 
    ORDER BY 1
    """, con)
    
    # Income band segmentation
    seg_income = pd.read_sql("""
    SELECT 
        c.income_band,
        ROUND(AVG(bt.default_60d), 3) AS default_rate,
        ROUND(AVG(bt.bill_amount), 2) AS avg_bill,
        COUNT(*) AS n_bills
    FROM bill_targets bt 
    JOIN customers c USING(customer_id) 
    GROUP BY c.income_band 
    ORDER BY default_rate DESC
    """, con)
    
    # Regional segmentation
    seg_region = pd.read_sql("""
    SELECT 
        c.region,
        ROUND(AVG(bt.default_60d), 3) AS default_rate,
        COUNT(*) AS n_bills
    FROM bill_targets bt 
    JOIN customers c USING(customer_id) 
    GROUP BY c.region 
    ORDER BY default_rate DESC
    """, con)
    
    # Collections actions distribution
    actions_dist = pd.read_sql("""
    SELECT 
        action,
        COUNT(*) as n
    FROM collections_actions 
    GROUP BY action 
    ORDER BY n DESC
    """, con)
    
    print(f"✓ Loaded {len(kpi_monthly)} months of data")
    print(f"✓ Loaded {len(seg_income)} income bands")
    print(f"✓ Loaded {len(seg_region)} regions")
    print(f"✓ Loaded {len(actions_dist)} action types")
    
    # Generate visualisations
    print("📈 Generating visualisations...")
    
    # 1) Monthly default rate trend
    plt.figure(figsize=(12, 6))
    plt.plot(kpi_monthly['month'], kpi_monthly['default_rate'], 
             marker='o', linewidth=2, markersize=6, color='#2E86AB')
    plt.title('Monthly Default Rate Trend', fontsize=16, fontweight='bold')
    plt.xlabel('Month', fontsize=12)
    plt.ylabel('Default Rate', fontsize=12)
    plt.xticks(rotation=45)
    plt.grid(True, alpha=0.3)
    plt.tight_layout()
    plt.savefig('outputs/figures/monthly_default_rate.png', dpi=200, bbox_inches='tight')
    plt.close()
    print("✓ Saved monthly_default_rate.png")
    
    # 2) Default rate by income band
    plt.figure(figsize=(10, 6))
    sns.barplot(data=seg_income, x='income_band', y='default_rate', 
                palette='viridis')
    plt.title('Default Rate by Income Band', fontsize=16, fontweight='bold')
    plt.xlabel('Income Band', fontsize=12)
    plt.ylabel('Default Rate', fontsize=12)
    plt.xticks(rotation=45)
    plt.tight_layout()
    plt.savefig('outputs/figures/default_by_income.png', dpi=200, bbox_inches='tight')
    plt.close()
    print("✓ Saved default_by_income.png")
    
    # 3) Default rate by region
    plt.figure(figsize=(12, 6))
    sns.barplot(data=seg_region, x='region', y='default_rate', 
                palette='plasma')
    plt.title('Default Rate by Region', fontsize=16, fontweight='bold')
    plt.xlabel('Region', fontsize=12)
    plt.ylabel('Default Rate', fontsize=12)
    plt.xticks(rotation=45, ha='right')
    plt.tight_layout()
    plt.savefig('outputs/figures/default_by_region.png', dpi=200, bbox_inches='tight')
    plt.close()
    print("✓ Saved default_by_region.png")
    
    # 4) Collections actions distribution
    plt.figure(figsize=(10, 6))
    sns.barplot(data=actions_dist, x='action', y='n', 
                palette='coolwarm')
    plt.title('Collections Actions Volume', fontsize=16, fontweight='bold')
    plt.xlabel('Action Type', fontsize=12)
    plt.ylabel('Number of Actions', fontsize=12)
    plt.xticks(rotation=20)
    plt.tight_layout()
    plt.savefig('outputs/figures/actions_distribution.png', dpi=200, bbox_inches='tight')
    plt.close()
    print("✓ Saved actions_distribution.png")
    
    # Display key insights
    print("\n📋 KEY INSIGHTS:")
    overall_default = kpi_monthly['default_rate'].mean()
    print(f"   Overall Portfolio Default Rate: {overall_default:.1%}")
    
    highest_risk_income = seg_income.iloc[0]
    print(f"   Highest risk income band: {highest_risk_income['income_band']} ({highest_risk_income['default_rate']:.1%})")
    
    highest_risk_region = seg_region.iloc[0]
    print(f"   Highest risk region: {highest_risk_region['region']} ({highest_risk_region['default_rate']:.1%})")
    
    total_actions = actions_dist['n'].sum()
    print(f"   Total collections actions: {total_actions:,}")
    
    print("\n🎉 Analysis complete! All figures saved to outputs/figures/")
    
finally:
    con.close()