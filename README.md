# Portfolio Collections Dashboard

**Goal:** Visualise arrears and default trends to support proactive collections. Reuses the same dataset as the Predicting Customer Payment Default Risk project.

## Data
- `data/customers.csv`
- `data/bills.csv`
- `data/payments.csv`
- `data/collections_actions.csv`
- `data/water_collections_demo.sqlite`

## What's Inside
- **Interactive Notebook**: [`notebooks/Portfolio_Collections_Dashboard.ipynb`](notebooks/Portfolio_Collections_Dashboard.ipynb)
  - 🎛️ **Interactive Dashboard** with widgets and plotly charts
  - 📊 Dynamic filtering by date range, metrics, and segments
  - 📈 Real-time chart updates and KPI gauges
- Static figures saved to `outputs/figures/` for this README

## Key Features
- **Interactive Dashboard**: Dynamic charts with date range sliders and metric selectors
- **Monthly default rate** trends (D-3 to D+60 window)
- **Segmentation analysis** by income band and region
- **Collections actions** distribution and volume tracking
- **KPI gauges** with performance thresholds

## Screenshots
### Monthly Default Rate
![Monthly Default Rate](outputs/figures/monthly_default_rate.png)

### Default by Income Band
![Default by Income](outputs/figures/default_by_income.png)

### Default by Region
![Default by Region](outputs/figures/default_by_region.png)

### Collections Actions Distribution
![Actions Distribution](outputs/figures/actions_distribution.png)

## How to Run
```bash
pip install -r requirements.txt
python -c "import sqlite3, pandas as pd; print('DB OK')"

# Launch Jupyter notebook for interactive dashboard
jupyter notebook notebooks/Portfolio_Collections_Dashboard.ipynb

# Or open in VS Code and run all cells
# Interactive widgets require Jupyter environment
```

## Interactive Dashboard Features
- 📅 **Date Range Slider**: Filter analysis to specific time periods
- 📊 **Metric Selector**: Switch between default rate, billed amounts, and paid amounts  
- 🎯 **Segmentation Toggle**: View analysis by income band or region
- ⚡ **Real-time Updates**: All charts update dynamically based on selections
- 🎛️ **KPI Gauges**: Performance indicators with thresholds

## Notes
- Uses the same dataset as Project 1 (risk model).
- Easily extended with cohort analysis, tariff-level views, and arrears £ balances.