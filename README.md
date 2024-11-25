---

# **📊 Stock Market Analysis and Forecasting Dashboard**

## **📖 Table of Contents**  
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
12. [📸 Dashboard Images](#dashboard-images)  

---

## **🔗 GitHub Repository**  
[GitHub Repository: StockMarket_Analysis](https://github.com/Nikitachatse/StockMarket_Analysis)  

### **📁 Repository Contents**  
- 🐍 Python scripts for data fetching, preprocessing, and machine learning model training.  
- 📂 Power BI files (.pbix) for the interactive dashboard.  
- 📝 Documentation for setting up and using the project.  
- 🖼️ Screenshots of the dashboard for a quick visual reference.  

---

## **📚 About the Project**  
The **Stock Market Analysis and Forecasting Dashboard** is an interactive Power BI tool that provides insights into the top 10 companies from the NASDAQ-100 index. The dashboard highlights 📈 stock trends, 📊 trading volumes, and key performance metrics.  

Additionally, the project features a machine learning model that uses **XGBoost regression** to forecast stock prices for the next seven days. Real-time stock data is fetched dynamically using the `yfinance` library, ensuring up-to-date analysis for decision-makers.  

### **🏢 Companies Analyzed**  
- Amazon  
- Apple  
- Meta (Facebook)  
- PayPal  
- Cisco  
- Microsoft  
- Google (Alphabet)  
- Intel Corporation  
- Tesla  
- NVIDIA  

---

## **🎯 Project Objectives**  
1. Provide a comprehensive visualization of key metrics and trends in the NASDAQ-100 stock market.  
2. Leverage machine learning to predict future stock prices.  
3. Enable dynamic updates in the dashboard using cloud-based data sources.  

---

## **🛠️ Technologies Used**  
- **📊 Power BI**: Interactive visualizations and insights.  
- **🐍 Python**: Data fetching, preprocessing, and machine learning.  
- **📡 yfinance**: Real-time stock data fetching.  
- **⚙️ scikit-learn**: Data preprocessing and model evaluation.  
- **🌟 XGBoost**: Regression model for stock price prediction.  
- **☁️ Cloud Integration**: Python scripts embedded in Power BI for real-time updates.  

---

## **📂 Data Source**  
Historical stock data was fetched using the `yfinance` library, covering daily stock performance from 1984 to the present. The dataset includes:  
- 📈 Opening and closing prices  
- 📉 High and low prices  
- 🔄 Trading volume  
- 📜 Adjusted prices  

---

## **✨ Dashboard Features**  
1. **🔄 Dynamic Data Integration**: Real-time updates via embedded Python scripts.  
2. **📊 Interactive Visualizations**:  
   - 📆 Stock price trends (daily, weekly, monthly).  
   - 📈 Trading volume comparisons.  
   - 🏆 Performance rankings based on percentage changes.  
3. **📈 Forecasting**: Predicted stock prices for the next seven days.  
4. **🔍 Detailed Insights**: Drill-through functionality for company-specific performance.  
5. **⚡ Cross-Filtering**: Seamless interaction between visualizations for exploratory analysis.  

---

## **🤖 Machine Learning Model**  
The machine learning pipeline utilizes an **XGBoost regression** model for forecasting.  

### **🚀 Model Workflow**  
1. **📋 Data Preprocessing**:  
   - Handling missing values and outliers.  
   - Feature normalization for improved model accuracy.  
2. **⚙️ Model Training and Validation**:  
   - Training the model on historical stock data.  
   - Evaluating performance using RMSE and MAE metrics.  
   - Hyperparameter tuning for robust predictions.  
3. **🔗 Integration with Power BI**:  
   - Embedding Python scripts to dynamically display forecasts.  

---

## **🛠️ How the Dashboard Works**  
1. **📡 Data Fetching**:  
   - Python scripts fetch live and historical stock data via the `yfinance` library.  
2. **📋 Data Processing**:  
   - Preprocessed data is input into the XGBoost model for predictions.  
3. **🔄 Dynamic Updates**:  
   - Embedded Python scripts refresh data and visuals in Power BI automatically.  
4. **👩‍💻 User Interaction**:  
   - Filters for company, time range, and performance metrics enable granular exploration.  

---

## **🚧 Challenges Faced**  
1. **📚 Large Data Volume**: Efficiently managing stock data spanning over three decades.  
2. **⚙️ Python-Power BI Integration**: Embedding Python scripts for real-time updates.  
3. **📊 Forecast Accuracy**: Balancing accuracy with computational efficiency for the XGBoost model.  

---

## **✅ Testing and Validation**  
- The machine learning model was validated using RMSE and MAE metrics to ensure accurate predictions.  
- The dashboard was rigorously tested for responsiveness, data accuracy, and cross-device compatibility.  

---

## **🔮 Future Scope**  
1. **🌍 Wider Coverage**: Incorporate additional indices and companies for more comprehensive analysis.  
2. **📰 Sentiment Analysis**: Integrate news and social media sentiment data for enhanced forecasting.  
3. **🗣️ Natural Language Queries**: Enable users to interact with the dashboard using conversational queries.  
4. **⚡ Performance Optimization**: Enhance loading times and scalability for larger datasets.  

---

## **🏁 Conclusion**  
This project demonstrates the power of combining analytics and machine learning to gain actionable insights into the stock market. With real-time updates and predictive capabilities, the dashboard is a valuable tool for investors and analysts.  

---

## **📸 Dashboard Images**  

### **Dashboard Image 1**  
![Dashboard Image 1](https://github.com/user-attachments/assets/dd7baea3-b47f-4c0d-8c49-12eb10767ad8)  

### **Dashboard Image 2**  
![Dashboard Image 2](https://github.com/user-attachments/assets/77034c43-ce7e-4898-a535-6fcc4048d7c7)  

---
