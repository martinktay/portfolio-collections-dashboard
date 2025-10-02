# Implementation Plan

- [x] 1. Set up project structure and directories


  - Create required directories: data/, notebooks/, outputs/figures/, assets/
  - Initialize directory structure for organized file management
  - _Requirements: 6.3_



- [ ] 2. Create and populate SQLite database
  - Import CSV files into SQLite database at data/water_collections_demo.sqlite
  - Implement data loading logic with proper error handling


  - Verify data integrity and referential relationships
  - _Requirements: 1.1, 4.4_

- [x] 3. Implement database performance optimizations


  - Create composite indexes on (customer_id, date) columns for bills, payments, collections_actions
  - Add index on bills(customer_id, bill_period_end) for efficient joins
  - Add index on payments(customer_id, payment_date) for payment window queries
  - _Requirements: 4.4_


- [ ] 4. Create KPI calculation SQL view
  - Implement bill_targets view with default rate logic (D-3 to D+60 payment window)
  - Handle payment matching with £1 tolerance for bill settlement
  - Include paid_in_window and default_60d calculated fields

  - _Requirements: 1.2, 1.3_

- [ ] 5. Build monthly trend analysis
  - Query bill_targets view to calculate monthly default rates
  - Aggregate billed and paid amounts by month

  - Create pandas DataFrame with month, default_rate, billed, paid columns
  - _Requirements: 1.3_

- [ ] 6. Implement customer segmentation analysis
  - Create income band segmentation query joining customers and bill_targets

  - Create region segmentation query with default rates by geographic area
  - Calculate average bill amounts and sample sizes for each segment
  - _Requirements: 2.1, 2.2_

- [ ] 7. Analyze collections actions distribution
  - Query collections_actions table to count action types

  - Create summary of Reminder Sent, Second Reminder, Arrangement Agreed, Arrangement Broken volumes
  - Prepare data for visualization
  - _Requirements: 3.1, 3.3_

- [ ] 8. Create monthly default rate visualization
  - Generate line plot with markers showing default rate trends over time

  - Apply seaborn styling for professional appearance
  - Add proper title, axis labels, and rotated x-axis dates
  - Save as PNG with DPI=200 to outputs/figures/monthly_default_rate.png
  - _Requirements: 1.4_

- [x] 9. Create income band segmentation chart

  - Generate horizontal bar chart showing default rates by income band
  - Sort by default rate descending for easy interpretation
  - Apply consistent styling and clear labels
  - Save as PNG to outputs/figures/default_by_income.png
  - _Requirements: 2.3, 2.4_

- [ ] 10. Create regional analysis visualization
  - Generate bar chart showing default rates by region
  - Handle long region names with rotated labels
  - Ensure all regions are visible and readable
  - Save as PNG to outputs/figures/default_by_region.png
  - _Requirements: 2.3, 2.4_




- [ ] 11. Create collections actions distribution chart
  - Generate bar chart showing volume of each action type
  - Include all action types with appropriate formatting
  - Add clear title and axis labels

  - Save as PNG to outputs/figures/actions_distribution.png
  - _Requirements: 3.2, 3.4_

- [ ] 12. Build comprehensive Jupyter notebook
  - Create notebook with structured markdown sections as specified

  - Implement all code blocks: imports, sanity checks, indexes, KPI views, tables, plots
  - Add markdown explanations between code sections
  - Display summary tables for key insights
  - _Requirements: 4.1, 4.2, 4.5_

- [ ] 13. Implement data validation and error handling
  - Add sanity checks for table row counts

  - Validate date formats and logical sequences
  - Handle missing data in payment matching logic
  - Add error handling for file operations and database connections
  - _Requirements: 4.2_

- [ ] 14. Create requirements.txt file
  - List all required Python packages: pandas, numpy, matplotlib, seaborn
  - Specify compatible versions for reproducibility
  - Include any additional dependencies discovered during development
  - _Requirements: 5.4_

- [ ] 15. Write comprehensive README.md
  - Create project description explaining goal and dataset reuse
  - Document data sources and file structure
  - Explain key KPIs and methodology
  - Add inline images for all four generated charts
  - Include setup and execution instructions


  - _Requirements: 5.1, 5.2, 5.3_


- [ ] 16. Verify all chart images display in README
  - Test that all PNG files are generated correctly
  - Confirm relative paths work for GitHub display




  - Verify image quality and readability
  - Check that charts load properly in GitHub preview
  - _Requirements: 5.1_

- [ ] 17. Initialize Git repository and commit files
  - Run git init to initialize repository
  - Add all project files to version control
  - Create initial commit with descriptive message
  - Set up main branch as default
  - _Requirements: 6.1, 6.4_

- [ ] 18. Configure GitHub remote and push
  - Remove any existing origin remote
  - Add GitHub remote for martinktay/Portfolio-Collections-Dashboard
  - Push all files to GitHub repository
  - Verify repository structure and file accessibility
  - _Requirements: 6.2_

- [ ] 19. Validate final deliverables
  - Confirm all four PNG files exist in outputs/figures/
  - Test notebook execution from clean environment
  - Verify README links resolve correctly on GitHub
  - Check that images display properly in GitHub README
  - _Requirements: 5.5_

- [ ] 20. Perform end-to-end testing
  - Clone repository to fresh directory
  - Install requirements and run notebook
  - Verify all outputs generate correctly
  - Confirm professional presentation quality for portfolio use
  - _Requirements: 4.2, 5.5_