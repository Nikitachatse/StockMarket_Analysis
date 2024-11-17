# Stock Market Analysis Dashboard

## Table of Contents
1. [About](#about)
2. [Project Objectives](#project-objectives)
3. [Technologies Used](#technologies-used)
4. [Data Source](#data-source)
5. [Dashboard Features](#dashboard-features)
6. [Machine Learning Model](#machine-learning-model)
7. [How the Dashboard Works](#how-the-dashboard-works)
8. [Conclusion](#conclusion)

---

## About

This project involves creating a dynamic and interactive Power BI dashboard for **stock market analysis**. The dashboard visualizes data for 10 top companies from the **NASDAQ-100 index** of the US stock market. It includes key insights such as price trends, volume changes, and stock performance. 

Additionally, we integrated a **machine learning model** to predict stock prices for the next seven days, providing a forward-looking perspective for decision-makers. The integration of the **yfinance** library ensures the data remains up-to-date by accessing cloud-based stock data dynamically through a Python script.

---

## Project Objectives

1. To visualize key metrics and trends in the NASDAQ-100 stock market.
2. To predict future stock prices using a machine learning model.
3. To make the Power BI dashboard dynamic by integrating cloud-based data sources.

---

## Technologies Used

- **Power BI**: For creating the interactive dashboard.
- **Python**: For data processing and machine learning.
  - **yfinance**: To fetch stock market data.
  - **scikit-learn**: For building the machine learning model.
- **Cloud Integration**: Accessed live stock data through Python scripts embedded in Power BI.

---

## Data Source

The stock market data for the top 10 companies in the **NASDAQ-100 index** was fetched using the `yfinance` Python library. This included daily historical data such as:
- Opening and closing prices
- High and low prices
- Volume traded

---

## Dashboard Features

1. **Dynamic Data Integration**: The dashboard updates automatically with the latest stock data using embedded Python scripts.
2. **Interactive Visualizations**:
   - Stock price trends (daily, weekly, monthly).
   - Volume comparisons across companies.
   - Performance rankings based on percentage changes.
3. **Machine Learning Predictions**: Displays forecasted stock prices for the next seven days for each company.
4. **Company-Specific Insights**: Drill-through functionality to view detailed analysis for individual companies.

---

## Machine Learning Model

We developed a **predictive model** to forecast stock prices using the historical data. The steps included:
1. Data preprocessing to handle missing values and normalize features.
2. Training a regression model using libraries like **scikit-learn**.
3. Testing the model on recent stock data for validation.
4. Integrating the predictions into the Power BI dashboard to display forecasted values dynamically.

---

## How the Dashboard Works

1. **Data Fetching**: A Python script fetches stock data using the `yfinance` library, ensuring up-to-date information.
2. **Data Processing**: The script preprocesses the data and generates predictions using the machine learning model.
3. **Power BI Integration**: The Python script is embedded into Power BI, linking the processed data to the visualizations.
4. **Dynamic Updates**: The dashboard refreshes automatically with each data fetch, ensuring real-time insights.

---

## Conclusion

This project successfully combines the power of **Power BI** and **Python** to deliver a comprehensive and dynamic stock market analysis dashboard. By integrating live data and machine learning predictions, the dashboard provides actionable insights into stock trends and future price movements for companies in the NASDAQ-100 index.
