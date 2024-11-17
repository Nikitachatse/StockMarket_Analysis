## **Stock Market Analysis and Forecasting Dashboard**

## Table of Contents  
1. [About the Project](#about-the-project)  
2. [Project Objectives](#project-objectives)  
3. [Technologies Used](#technologies-used)  
4. [Data Source](#data-source)  
5. [Dashboard Features](#dashboard-features)  
6. [Machine Learning Model](#machine-learning-model)  
7. [How the Dashboard Works](#how-the-dashboard-works)  
8. [Challenges Faced](#challenges-faced)  
9. [Testing and Validation](#testing-and-validation)  
10. [Future Scope](#future-scope)  
11. [Conclusion](#conclusion)

---

### **Git Repository**
[GitHub Repository: StockMarket_Analysis](https://github.com/Nikitachatse/StockMarket_Analysis)  
The repository contains:
- Python scripts for data fetching, preprocessing, and machine learning model training.
- Power BI files (.pbix) for the interactive dashboard.
- Documentation explaining how to set up and use the project.
- Screenshots of the dashboard for a quick visual reference.

---

### **About the Project**
This project involves creating a dynamic and interactive Power BI dashboard for stock market analysis and forecasting. The dashboard visualizes data for the top 10 companies from the NASDAQ-100 index of the US stock market, providing key insights into stock trends, volumes, and performance metrics.

The companies analyzed include:
- **Amazon**
- **Apple**
- **Meta (Facebook)**
- **PayPal**
- **Cisco**
- **Microsoft**
- **Google (Alphabet)**
- **Intel Corporation**
- **Tesla**
- **NVIDIA**

Additionally, a machine learning model using XGBoost regression predicts stock prices for the next seven days, giving a forward-looking perspective for decision-makers. The integration of the `yfinance` library ensures real-time updates by accessing cloud-based stock data dynamically through a Python script.

---

### **Project Objectives**
1. Visualize key metrics and trends in the NASDAQ-100 stock market.
2. Predict future stock prices using an XGBoost regression model.
3. Enable dynamic updates in the Power BI dashboard using cloud-based data sources.

---

### **Technologies Used**
- **Power BI**: For creating interactive visualizations and insights.
- **Python**: For data fetching, processing, and machine learning.
- **yfinance**: For accessing historical and live stock data.
- **scikit-learn**: For preprocessing and evaluating the machine learning model.
- **XGBoost**: The regression model used for predicting stock prices.
- **Cloud Integration**: Embedded Python scripts in Power BI to dynamically fetch and update data.

---

### **Data Source**
Historical stock market data was fetched using the `yfinance` Python library. The dataset includes daily data from 1981 to the present for the top 10 companies listed above. The data consists of:
- Opening and closing prices
- High and low prices
- Volume traded
- Adjusted prices

---

### **Dashboard Features**
1. **Dynamic Data Integration**: The dashboard updates automatically with the latest stock data through embedded Python scripts.
2. **Interactive Visualizations**:
   - Line charts for stock price trends (daily, weekly, monthly).
   - Volume comparisons across companies.
   - Performance rankings based on percentage changes.
3. **Machine Learning Predictions**: Forecasted stock prices for the next seven days for each company.
4. **Company-Specific Insights**: Drill-through functionality to explore individual companies' performance in detail.
5. **Cross-Filtering**: Seamless interaction between visualizations for intuitive exploration.

---

### **Machine Learning Model**
The XGBoost regression model was used to predict future stock prices based on historical trends. The development process involved:
1. **Data Preprocessing**:
   - Handling missing values and outliers.
   - Normalizing features to improve model accuracy.
2. **Model Training and Validation**:
   - Training the XGBoost model on historical data.
   - Evaluating performance using metrics like RMSE and MAE.
   - Achieving robust predictions by tuning hyperparameters.
3. **Power BI Integration**:
   - Embedding Python scripts in Power BI to integrate predictions dynamically.
   - Displaying forecasted stock prices as interactive visuals.

---

### **How the Dashboard Works**
1. **Data Fetching**:
   - A Python script fetches historical and live stock data using the `yfinance` library.
   - Data from 1981 to the current date is processed.
2. **Data Processing**:
   - The script preprocesses the data and feeds it into the XGBoost model for predictions.
3. **Dynamic Updates**:
   - Embedded Python scripts in Power BI refresh data and visuals automatically.
4. **Interactive Features**:
   - Users can filter by company, time range, or performance metrics for granular insights.

---

### **Challenges Faced**
1. **Handling Large Data Volumes**: Processing data from 1981 required efficient memory management and preprocessing techniques.
2. **Integrating Python with Power BI**: Embedding Python scripts for real-time data updates posed technical challenges.
3. **Ensuring Forecast Accuracy**: Fine-tuning the XGBoost model to balance accuracy and runtime performance.

---

### **Testing and Validation**
- The machine learning model was validated using RMSE and MAE to ensure reliable predictions.
- The dashboard was tested for responsiveness, data accuracy, and usability across different devices and screen sizes.

---

### **Future Scope**
1. **Expanding Coverage**: Add more companies or indices for broader insights.
2. **Sentiment Analysis**: Integrate news and social media sentiment analysis for additional predictive factors.
3. **Enhanced Interactivity**: Add natural language query capabilities for user-friendly data exploration.
4. **Performance Optimization**: Improve dashboard loading times and model runtime for larger datasets.

---

### **Conclusion**
This project successfully combines the analytical power of Power BI and Python with machine learning to deliver actionable insights into the NASDAQ-100 index. By leveraging real-time data and predictive analytics, the dashboard empowers stakeholders to make informed investment decisions.

---
