# Technology Stack

## Core Technologies
- **Python**: Primary development language
- **Jupyter Notebook**: Interactive development and presentation environment
- **SQLite**: Local database for efficient analytical queries
- **Pandas**: Data manipulation and analysis
- **Matplotlib/Seaborn**: Professional visualization and charting

## Data Pipeline
- **Input**: CSV files (customers, bills, payments, collections_actions)
- **Processing**: SQLite database with optimized indexes and analytical views
- **Output**: PNG charts and Jupyter notebook with embedded analysis

## File Structure
- `data/customers.csv` - Master customer data with demographics and account settings
- `data/bills.csv` - Billing records with usage and amounts
- `data/payments.csv` - Payment transaction history
- `data/collections_actions.csv` - Debt collection activity tracking
- `data/water_collections_demo.sqlite` - SQLite database for analysis

## Data Standards
- **Date Format**: YYYY-MM-DD (ISO 8601)
- **Currency**: GBP (£) with decimal precision to 2 places
- **Customer IDs**: Format C100000+ (6-digit numeric with C prefix)
- **Boolean Fields**: 1/0 for binary flags (has_meter, is_vulnerable, prefers_direct_debit)

## Key Dependencies
```
pandas>=1.3.0
numpy>=1.20.0
matplotlib>=3.4.0
seaborn>=0.11.0
```

## Common Commands
```bash
# Install dependencies
pip install -r requirements.txt

# Run notebook (Jupyter)
jupyter notebook notebooks/Portfolio_Collections_Dashboard.ipynb

# Run notebook (VS Code)
# Open .ipynb file and run all cells

# Verify database
python -c "import sqlite3, pandas as pd; print('DB OK')"
```

## Performance Optimizations
- **Database Indexes**: Composite indexes on (customer_id, date) columns
- **SQL Views**: Pre-calculated KPIs for efficient querying
- **Chart Export**: High-quality PNG generation (DPI=200) for GitHub display