# Design Document

## Overview

The Portfolio Collections Dashboard is a Jupyter notebook-based analytics solution that provides visual insights into water utility collections performance. The design leverages existing CSV data, SQLite for efficient querying, and matplotlib/seaborn for professional visualizations suitable for GitHub portfolio presentation.

## Architecture

### Data Layer
- **Input**: Four CSV files (customers, bills, payments, collections_actions) 
- **Processing**: SQLite database with optimized indexes for analytical queries
- **Storage**: Local SQLite file (`data/water_collections_demo.sqlite`)

### Analytics Layer
- **KPI Engine**: SQL views for complex business logic (default rate calculations)
- **Segmentation**: Pandas-based aggregations by customer demographics
- **Time Series**: Monthly trend analysis with date-based grouping

### Presentation Layer
- **Notebook**: Jupyter notebook with structured markdown sections
- **Visualizations**: Publication-quality charts using seaborn styling
- **Export**: PNG files optimized for GitHub README display

## Components and Interfaces

### Database Schema
```sql
-- Core tables (from CSV import)
customers (customer_id, region, income_band, tariff, has_meter, is_vulnerable, prefers_direct_debit, tenure_band)
bills (customer_id, bill_period_end, bill_amount, usage_m3, due_date)
payments (customer_id, payment_date, amount, method)
collections_actions (customer_id, action_date, action)

-- Analytical view
bill_targets (customer_id, bill_period_end, due_date, bill_amount, paid_in_window, default_60d)
```

### KPI Calculation Logic
- **Default Definition**: Bill not paid within D-3 to D+60 window (allowing 3-day grace period, 60-day collection window)
- **Payment Matching**: Sum payments in window, compare to bill amount with £1 tolerance
- **Aggregation**: Monthly, by income band, by region

### Visualization Components

#### 1. Monthly Default Rate Trend
- **Type**: Line plot with markers
- **Data**: Time series aggregation by month
- **Purpose**: Identify seasonal patterns and portfolio trends
- **Export**: `monthly_default_rate.png`

#### 2. Default Rate by Income Band
- **Type**: Horizontal bar chart
- **Data**: Customer segmentation analysis
- **Purpose**: Identify socioeconomic risk factors
- **Export**: `default_by_income.png`

#### 3. Default Rate by Region
- **Type**: Bar chart with rotated labels
- **Data**: Geographic segmentation
- **Purpose**: Regional performance comparison
- **Export**: `default_by_region.png`

#### 4. Collections Actions Distribution
- **Type**: Bar chart showing action volumes
- **Data**: Action type frequency analysis
- **Purpose**: Understand intervention patterns
- **Export**: `actions_distribution.png`

## Data Models

### KPI Data Model
```python
# Monthly KPIs
kpi_monthly = {
    'month': str,           # YYYY-MM format
    'default_rate': float,  # 0.0 to 1.0
    'billed': float,        # Total amount billed
    'paid': float          # Total amount paid in window
}

# Segmentation Models
seg_income = {
    'income_band': str,     # e.g., "£15k-£30k"
    'default_rate': float,  # Rounded to 3 decimals
    'avg_bill': float,      # Average bill amount
    'n_bills': int         # Sample size
}

seg_region = {
    'region': str,          # e.g., "London - North"
    'default_rate': float,  # Rounded to 3 decimals
    'n_bills': int         # Sample size
}
```

## Error Handling

### Data Validation
- **Missing Data**: Handle NULL values in payment matching logic
- **Date Parsing**: Ensure consistent date formats across CSV imports
- **Amount Validation**: Check for negative amounts and handle edge cases

### Performance Optimization
- **Database Indexes**: Create composite indexes on (customer_id, date) columns
- **Query Optimization**: Use SQL views for complex calculations
- **Memory Management**: Process data in chunks if datasets grow large

### File System
- **Directory Creation**: Ensure output directories exist before saving figures
- **Path Handling**: Use relative paths for cross-platform compatibility
- **Image Quality**: Set DPI=200 for high-quality GitHub display

## Testing Strategy

### Data Quality Tests
- **Referential Integrity**: Verify all customer_ids exist in customers table
- **Date Logic**: Confirm bill_period_end < due_date relationships
- **Amount Consistency**: Check payment amounts are positive

### Visualization Tests
- **Chart Generation**: Verify all four PNG files are created
- **Data Accuracy**: Spot-check calculated default rates against manual calculations
- **Image Quality**: Confirm charts are readable and properly formatted

### Integration Tests
- **Notebook Execution**: Run all cells without errors
- **File Dependencies**: Verify all required files exist and are accessible
- **GitHub Integration**: Test README image links and notebook links

## Deployment Considerations

### GitHub Repository Structure
```
Portfolio-Collections-Dashboard/
├── data/
│   ├── customers.csv
│   ├── bills.csv
│   ├── payments.csv
│   ├── collections_actions.csv
│   └── water_collections_demo.sqlite
├── notebooks/
│   └── Portfolio_Collections_Dashboard.ipynb
├── outputs/
│   └── figures/
│       ├── monthly_default_rate.png
│       ├── default_by_income.png
│       ├── default_by_region.png
│       └── actions_distribution.png
├── assets/
├── requirements.txt
└── README.md
```

### Dependencies
- **Core**: pandas, numpy, matplotlib, seaborn
- **Database**: sqlite3 (built-in)
- **Environment**: Python 3.7+ compatible

### Performance Targets
- **Notebook Runtime**: < 30 seconds for full execution
- **Image Generation**: < 5 seconds per chart
- **Database Queries**: < 1 second per KPI calculation