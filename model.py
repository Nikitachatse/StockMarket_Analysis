import yfinance as yf
import pandas as pd
import numpy as np
from ta.momentum import RSIIndicator
from ta.trend import SMAIndicator
from xgboost import XGBRegressor
from sklearn.model_selection import train_test_split
from sklearn.metrics import mean_absolute_error
import joblib

# List of companies you want to analyze
companies = ['AAPL', 'MSFT', 'GOOGL', 'META', 'NVDA', 'AMZN', 'TSLA', 'PYPL', 
    'INTC', 'CSCO']

# Fetch historical data and create features
def fetch_and_prepare_data(tickers):
    all_data = pd.DataFrame()
    for ticker in tickers:
        stock_data = yf.download(ticker, period='10y')  # Last 5 years of data
        stock_data['Company'] = ticker
        
        # Feature engineering (e.g., moving averages, RSI)
        stock_data['SMA_10'] = stock_data['Close'].rolling(window=10).mean()
        stock_data['SMA_50'] = stock_data['Close'].rolling(window=50).mean()
        stock_data['RSI'] = RSIIndicator(stock_data['Close']).rsi()
        stock_data['y_lag1'] = stock_data['Close'].shift(1)
        stock_data['Volume_Lag1'] = stock_data['Volume'].shift(1)
        
        # Drop NaN values created by rolling features
        stock_data.dropna(inplace=True)
        
        all_data = pd.concat([all_data, stock_data])
    
    return all_data

data = fetch_and_prepare_data(companies)

# Prepare features (X) and target (y)
X = data[['SMA_10', 'SMA_50', 'RSI', 'Volume_Lag1', 'y_lag1']]
y = data['Close']

# Split data into train and test sets
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, shuffle=False)

# Train an XGBoost model
model = XGBRegressor(n_estimators=100, max_depth=5, learning_rate=0.1)
model.fit(X_train, y_train)

# Evaluate the model
y_pred = model.predict(X_test)
mae = mean_absolute_error(y_test, y_pred)
print(f"Mean Absolute Error (MAE): {mae}")

# Save the trained model
joblib.dump(model, 'stock_price_predictor_model.pkl')
