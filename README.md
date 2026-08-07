# E-Commerce Sales & Customer Analytics

An end-to-end data analytics project simulating a multi-category Indian
e-commerce company, covering the full pipeline from raw data to an
interactive Power BI dashboard.

## Business Problem
The (simulated) company wants to understand revenue trends, category
performance, return patterns, and customer behavior across Indian cities
to guide inventory, marketing, and logistics decisions.

## Objectives
- Model and query relational e-commerce data using SQL
- Clean and analyze transactional data using Python/Pandas
- Visualize trends and patterns through EDA
- Build an interactive Power BI dashboard for stakeholders
- Translate findings into actionable business recommendations

## Dataset
Synthetic dataset simulating ~9,000 orders across 600 customers, 35
products in 6 categories, spanning Jan 2023 – Jul 2025, across 20 Indian
cities. Includes intentional real-world data quality issues (missing
values, duplicates, inconsistent casing) to demonstrate cleaning
workflows.

| File | Description |
|---|---|
| `data/customers.csv` | Customer master data |
| `data/products.csv` | Product catalog |
| `data/orders_fresh.csv` | Raw order transactions |
| `data/orders_cleaned.csv` | Cleaned order transactions (post-Python cleaning) |
| `data/returns.csv` | Return records |

## Tools Used
- **SQL:** MySQL Workbench 8.0 — schema design, joins, subqueries, CTEs, window functions, views
- **Python:** Pandas, Matplotlib — data cleaning, EDA
- **Excel:** Initial data exploration
- **Power BI Desktop:** Interactive dashboard, DAX measures
- **GitHub:** Version control, portfolio hosting

## Workflow
Raw Dataset → Excel Exploration → SQL Database & Analysis → Python
Cleaning & EDA → Business Insights → Power BI Dashboard → Documentation

## SQL Work
See `/sql` — covers filtering & aggregation, joins/subqueries/CTEs,
window functions (RANK, running totals), and reusable views.

## Python Work
See `/python` — covers fundamentals, Pandas exploration, GroupBy/Merge,
missing value & duplicate handling, and EDA visualizations.

## Power BI Dashboard
See `/powerbi` for the `.pbix` file and `/screenshots` for a visual preview.

![Dashboard Overview](screenshots/dashboard-overview.png)

**Key measures:** Total Revenue, Total Profit, Profit Margin %,
Return Rate %, Average Order Value, Cancelled Orders %

## Business Insights
Full write-up in `/reports/business_insights.md`. Highlights:
- Total Revenue: ₹[your number]
- Total Profit: ₹[your number]
- Return Rate: [your number]%
- [Top category] drives the highest revenue at ₹[amount]
- [Top cities] account for [X]% of total revenue — geographic concentration
  worth monitoring

## Future Improvements
- Automate the SQL → Power BI refresh with a scheduled pipeline
- Add cohort/retention analysis for repeat customers
- Expand to a live/streaming data source instead of a static snapshot

## How to Run
1. Import `/data` CSVs into MySQL using `/sql/*.sql` scripts to recreate the schema
2. Run `/python` scripts in order (01 → 05) to reproduce cleaning and EDA
3. Open `/powerbi/ecommerce_dashboard.pbix` in Power BI Desktop (requires
   the MySQL database running locally to refresh)

## Folder Structure
ecommerce-sales-analytics-india/
│
├── data/
├── sql/
├── python/
├── powerbi/
├── reports/
├── screenshots/
└── README.md

## Interview Talking Points
- Designed a normalized relational schema (4 tables, PK/FK constraints)
- Wrote SQL covering joins, subqueries, CTEs, and window functions
  (RANK/DENSE_RANK/ROW_NUMBER)
- Diagnosed and fixed a real locale-based date formatting bug during import
- Applied Pandas for cleaning (missing values, duplicates, casing) with
  documented, repeatable logic
- Built a Power BI star-schema data model with custom DAX measures
- Translated chart-level findings into hedged, business-appropriate
  recommendations
