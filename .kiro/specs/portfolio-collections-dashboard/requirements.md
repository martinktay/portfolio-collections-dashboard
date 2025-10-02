# Requirements Document

## Introduction

This project creates a Portfolio Collections Dashboard for a water utility company to visualize arrears and default trends, supporting proactive collections management. The dashboard reuses the existing dataset from the customer payment default risk project and will be published to GitHub as a portfolio piece.

## Requirements

### Requirement 1

**User Story:** As a collections manager, I want to view monthly default rate trends, so that I can identify seasonal patterns and overall portfolio performance.

#### Acceptance Criteria

1. WHEN I open the dashboard notebook THEN the system SHALL load data from the SQLite database containing customers, bills, payments, and collections_actions tables
2. WHEN the system calculates default rates THEN it SHALL use a D-3 to D+60 payment window (3 days before due date to 60 days after)
3. WHEN displaying monthly trends THEN the system SHALL show default rates aggregated by month with clear visualization
4. WHEN I view the monthly default rate chart THEN it SHALL be saved as a PNG file for README inclusion

### Requirement 2

**User Story:** As a collections analyst, I want to segment default rates by customer demographics, so that I can identify high-risk customer segments.

#### Acceptance Criteria

1. WHEN analyzing customer segments THEN the system SHALL calculate default rates by income band
2. WHEN analyzing customer segments THEN the system SHALL calculate default rates by region
3. WHEN displaying segmentation results THEN the system SHALL show clear bar charts with default rates
4. WHEN I view segmentation charts THEN they SHALL be saved as PNG files with appropriate titles and formatting

### Requirement 3

**User Story:** As a collections team lead, I want to understand collections activity distribution, so that I can optimize our intervention strategies.

#### Acceptance Criteria

1. WHEN analyzing collections actions THEN the system SHALL count occurrences of each action type
2. WHEN displaying action distribution THEN the system SHALL show a bar chart of action volumes
3. WHEN I view the actions chart THEN it SHALL include all action types (Reminder Sent, Second Reminder, Arrangement Agreed, Arrangement Broken)
4. WHEN the chart is generated THEN it SHALL be saved as a PNG file for documentation

### Requirement 4

**User Story:** As a portfolio manager, I want a comprehensive notebook with all analysis and insights, so that I can reproduce and extend the analysis.

#### Acceptance Criteria

1. WHEN I open the notebook THEN it SHALL contain clearly structured sections with markdown headers
2. WHEN running the notebook THEN it SHALL execute without errors and display all visualizations
3. WHEN the analysis completes THEN it SHALL save all figures to the outputs/figures directory
4. WHEN I review the code THEN it SHALL include proper database indexing for performance
5. WHEN the notebook runs THEN it SHALL display summary tables for key insights

### Requirement 5

**User Story:** As a GitHub visitor, I want a polished README with screenshots, so that I can understand the project value and see the results.

#### Acceptance Criteria

1. WHEN I visit the GitHub repository THEN the README SHALL display all four generated charts inline
2. WHEN I read the README THEN it SHALL explain the project goal, data sources, and key KPIs
3. WHEN I want to run the project THEN the README SHALL provide clear setup instructions
4. WHEN viewing the repository THEN it SHALL include a requirements.txt file with all dependencies
5. WHEN I click on notebook links THEN they SHALL resolve correctly to the notebook file

### Requirement 6

**User Story:** As a developer, I want the project properly version controlled and published, so that it serves as a professional portfolio piece.

#### Acceptance Criteria

1. WHEN the project is complete THEN it SHALL be initialized as a Git repository
2. WHEN publishing THEN it SHALL be pushed to the specified GitHub repository (martinktay/Portfolio-Collections-Dashboard)
3. WHEN I view the repository structure THEN it SHALL follow the defined directory layout with data/, notebooks/, outputs/figures/, and assets/ folders
4. WHEN the project is committed THEN it SHALL include all deliverable files with appropriate commit messages