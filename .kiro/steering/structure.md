# Project Structure

## Root Directory Layout
```
Portfolio-Collections-Dashboard/
├── data/                           # Data files and database
│   ├── customers.csv              # Master customer data
│   ├── bills.csv                  # Billing records
│   ├── payments.csv               # Payment transactions
│   ├── collections_actions.csv   # Collections activity
│   └── water_collections_demo.sqlite # SQLite database
├── notebooks/                      # Jupyter notebooks
│   └── Portfolio_Collections_Dashboard.ipynb
├── outputs/                        # Generated outputs
│   └── figures/                   # Chart exports for README
│       ├── monthly_default_rate.png
│       ├── default_by_income.png
│       ├── default_by_region.png
│       └── actions_distribution.png
├── assets/                         # Additional assets
├── .kiro/                         # Kiro configuration
│   ├── steering/                  # AI assistant guidance
│   └── specs/                     # Project specifications
├── requirements.txt               # Python dependencies
└── README.md                      # Project documentation
```

## Key Directories

### data/
Contains all source data and the analytical database:
- **CSV files**: Original data sources from the payment default risk project
- **SQLite database**: Optimized for analytical queries with indexes and views
- **Data integrity**: All files use customer_id as the primary relationship key

### notebooks/
Contains the main analytical notebook:
- **Portfolio_Collections_Dashboard.ipynb**: Complete analysis with visualizations
- **Structured sections**: Setup, KPIs, EDA, insights, conclusions
- **Executable**: Designed to run end-to-end without errors

### outputs/figures/
Generated visualizations for GitHub README:
- **High-quality PNGs**: DPI=200 for professional presentation
- **Consistent styling**: Seaborn theme with clear titles and labels
- **GitHub-optimized**: Relative paths for proper README display

## Data Relationships
- **customer_id**: Primary key linking all datasets
- **Time-based**: Bills → Payments → Collections sequence
- **Analytical views**: SQL views for complex KPI calculations
- **Segmentation**: Customer demographics drive risk analysis

## Naming Conventions
- **Directories**: lowercase with underscores or hyphens
- **Files**: descriptive names reflecting content and purpose
- **Charts**: descriptive names matching their analytical purpose
- **Variables**: snake_case for Python code consistency