#!/usr/bin/env python3
"""
Standalone demo of the interactive dashboard
This shows the dashboard working outside of Jupyter
"""
import sqlite3
import pandas as pd
import plotly.express as px
import plotly.graph_objects as go
from plotly.subplots import make_subplots

def demo_interactive_dashboard():
    """Demonstrate the interactive dashboard functionality"""
    
    print("🚀 PORTFOLIO COLLECTIONS DASHBOARD DEMO")
    print("=" * 50)
    
    # Load data
    con = sqlite3.connect('data/water_collections_demo.sqlite')
    
    monthly_data = pd.read_sql("""
    SELECT 
        strftime('%Y-%m', bill_period_end) AS month,
        AVG(default_60d) AS default_rate,
        SUM(bill_amount) AS total_billed,
        SUM(paid_in_window) AS total_paid,
        COUNT(*) as bill_count
    FROM bill_targets 
    GROUP BY 1 
    ORDER BY 1
    """, con)
    
    income_data = pd.read_sql("""
    SELECT 
        c.income_band,
        ROUND(AVG(bt.default_60d), 3) AS default_rate,
        COUNT(*) AS bills,
        COUNT(DISTINCT bt.customer_id) AS customers
    FROM bill_targets bt 
    JOIN customers c USING(customer_id) 
    GROUP BY c.income_band 
    ORDER BY default_rate DESC
    """, con)
    
    region_data = pd.read_sql("""
    SELECT 
        c.region,
        ROUND(AVG(bt.default_60d), 3) AS default_rate,
        COUNT(*) AS bills
    FROM bill_targets bt 
    JOIN customers c USING(customer_id) 
    GROUP BY c.region 
    ORDER BY default_rate DESC
    """, con)
    
    actions_data = pd.read_sql("""
    SELECT 
        action,
        COUNT(*) as count
    FROM collections_actions 
    GROUP BY action 
    ORDER BY count DESC
    """, con)
    
    con.close()
    
    print(f"📊 Data loaded successfully:")
    print(f"   📅 Monthly data: {len(monthly_data)} months")
    print(f"   💰 Income segments: {len(income_data)} bands")
    print(f"   🌍 Regions: {len(region_data)} areas")
    print(f"   📞 Action types: {len(actions_data)} categories")
    
    # Show sample data
    print("\\n📋 SAMPLE DATA TABLES:")
    print("\\nMonthly KPIs (first 5 months):")
    print(monthly_data.head().to_string(index=False))
    
    print("\\nIncome Band Analysis:")
    print(income_data.to_string(index=False))
    
    print("\\nRegional Analysis:")
    print(region_data.to_string(index=False))
    
    print("\\nCollections Actions:")
    print(actions_data.to_string(index=False))
    
    # Generate key insights
    print("\\n" + "=" * 50)
    print("🎯 KEY INSIGHTS")
    print("=" * 50)
    
    overall_default_rate = monthly_data['default_rate'].mean()
    total_billed = monthly_data['total_billed'].sum()
    total_paid = monthly_data['total_paid'].sum()
    collection_rate = total_paid / total_billed
    
    print(f"📊 Portfolio Performance:")
    print(f"   Overall Default Rate: {overall_default_rate:.1%}")
    print(f"   Total Billed: £{total_billed:,.0f}")
    print(f"   Total Collected: £{total_paid:,.0f}")
    print(f"   Collection Rate: {collection_rate:.1%}")
    
    highest_risk_income = income_data.iloc[0]
    lowest_risk_income = income_data.iloc[-1]
    highest_risk_region = region_data.iloc[0]
    
    print(f"\\n🎯 Risk Segments:")
    print(f"   Highest Risk Income: {highest_risk_income['income_band']} ({highest_risk_income['default_rate']:.1%})")
    print(f"   Lowest Risk Income: {lowest_risk_income['income_band']} ({lowest_risk_income['default_rate']:.1%})")
    print(f"   Highest Risk Region: {highest_risk_region['region']} ({highest_risk_region['default_rate']:.1%})")
    
    total_actions = actions_data['count'].sum()
    most_common_action = actions_data.iloc[0]
    
    print(f"\\n📞 Collections Activity:")
    print(f"   Total Actions: {total_actions:,}")
    print(f"   Most Common: {most_common_action['action']} ({most_common_action['count']:,} times)")
    
    # Create and show interactive charts (they will open in browser)
    print("\\n" + "=" * 50)
    print("📈 GENERATING INTERACTIVE CHARTS")
    print("=" * 50)
    
    # 1. Monthly trend chart
    fig1 = px.line(
        monthly_data,
        x='month',
        y='default_rate',
        title='📈 Monthly Default Rate Trend (Interactive)',
        markers=True,
        hover_data=['total_billed', 'total_paid', 'bill_count']
    )
    fig1.update_layout(title_x=0.5, hovermode='x unified')
    print("✅ Created monthly trend chart")
    
    # 2. Income band analysis
    fig2 = px.bar(
        income_data,
        x='income_band',
        y='default_rate',
        title='💰 Default Rate by Income Band (Interactive)',
        color='default_rate',
        color_continuous_scale='Viridis',
        hover_data=['bills', 'customers']
    )
    fig2.update_layout(title_x=0.5)
    print("✅ Created income band chart")
    
    # 3. Regional analysis
    fig3 = px.bar(
        region_data,
        x='region',
        y='default_rate',
        title='🌍 Default Rate by Region (Interactive)',
        color='default_rate',
        color_continuous_scale='Plasma',
        hover_data=['bills']
    )
    fig3.update_layout(title_x=0.5, xaxis_tickangle=-45)
    print("✅ Created regional analysis chart")
    
    # 4. Collections actions pie chart
    fig4 = px.pie(
        actions_data,
        values='count',
        names='action',
        title='📞 Collections Actions Distribution (Interactive)'
    )
    fig4.update_layout(title_x=0.5)
    print("✅ Created collections actions chart")
    
    # 5. Multi-panel dashboard
    fig_dashboard = make_subplots(
        rows=2, cols=2,
        subplot_titles=('Monthly Default Rate', 'Income Band Analysis', 'Regional Analysis', 'Collections Actions'),
        specs=[[{"secondary_y": False}, {"secondary_y": False}],
               [{"secondary_y": False}, {"type": "pie"}]]
    )
    
    # Add traces to dashboard
    fig_dashboard.add_trace(
        go.Scatter(x=monthly_data['month'], y=monthly_data['default_rate'], 
                  mode='lines+markers', name='Default Rate'),
        row=1, col=1
    )
    
    fig_dashboard.add_trace(
        go.Bar(x=income_data['income_band'], y=income_data['default_rate'], 
               name='Income Bands'),
        row=1, col=2
    )
    
    fig_dashboard.add_trace(
        go.Bar(x=region_data['region'], y=region_data['default_rate'], 
               name='Regions'),
        row=2, col=1
    )
    
    fig_dashboard.add_trace(
        go.Pie(labels=actions_data['action'], values=actions_data['count'], 
               name='Actions'),
        row=2, col=2
    )
    
    fig_dashboard.update_layout(
        height=800,
        title_text="🎛️ Portfolio Collections Dashboard",
        title_x=0.5,
        showlegend=False
    )
    print("✅ Created comprehensive dashboard")
    
    print("\\n" + "=" * 50)
    print("🎉 DEMO COMPLETE!")
    print("=" * 50)
    
    print("\\n📊 What was demonstrated:")
    print("   ✅ Data loading from SQLite database")
    print("   ✅ Data processing and analysis")
    print("   ✅ Interactive chart creation with plotly")
    print("   ✅ Comprehensive data tables")
    print("   ✅ Key business insights generation")
    print("   ✅ Multi-panel dashboard creation")
    
    print("\\n🎛️ Interactive Features Available:")
    print("   • Hover over data points for detailed information")
    print("   • Zoom in/out using mouse wheel or controls")
    print("   • Pan across charts by clicking and dragging")
    print("   • Double-click to reset zoom")
    print("   • Click legend items to show/hide data")
    
    print("\\n🚀 To run the full interactive dashboard:")
    print("   1. Install Jupyter: pip install jupyter")
    print("   2. Launch notebook: jupyter notebook notebooks/Portfolio_Collections_Dashboard.ipynb")
    print("   3. Run all cells and use the dropdown controls")
    
    # Optionally show charts (uncomment to display in browser)
    # fig1.show()
    # fig2.show()
    # fig3.show()
    # fig4.show()
    # fig_dashboard.show()
    
    return True

if __name__ == "__main__":
    demo_interactive_dashboard()