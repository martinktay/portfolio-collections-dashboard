# Portfolio Collections Dashboard

**Goal:** Visualise arrears and default trends to support proactive collections. Reuses the same dataset as the Predicting Customer Payment Default Risk project.

## Data
- `data/customers.csv`
- `data/bills.csv`
- `data/payments.csv`
- `data/collections_actions.csv`
- `data/water_collections_demo.sqlite`

## What's Inside
- Notebook: [`notebooks/Portfolio_Collections_Dashboard.ipynb`](notebooks/Portfolio_Collections_Dashboard.ipynb)
- Figures saved to `outputs/figures/` for this README

## Key Views & KPIs
- **Monthly default rate** (D-3 to D+60 window)
- **Default by income band / region**
- **Collections actions distribution**

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
# or open the notebook in Jupyter/VS Code and run all cells
```

## Notes
- Uses the same dataset as Project 1 (risk model).
- Easily extended with cohort analysis, tariff-level views, and arrears £ balances.