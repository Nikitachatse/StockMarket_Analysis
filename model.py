import pandas as pd
import yfinance as yf
import joblib
from ta.momentum import RSIIndicator
from ta.trend import SMAIndicator

# Load the trained model
model = joblib.load(r"C:\Users\chats\notes\stock_price_predictor_model.pkl")

# Function to get historical stock data with indicators
def get_company_data(ticker, lookback_days=50):
    stock_data = yf.download(ticker, period='3mo')  
    stock_data['SMA_10'] = stock_data['Close'].rolling(window=10).mean()
    stock_data['SMA_50'] = stock_data['Close'].rolling(window=50).mean()
    stock_data['RSI'] = RSIIndicator(stock_data['Close']).rsi()
    stock_data['y_lag1'] = stock_data['Close'].shift(1)
    stock_data['Volume_Lag1'] = stock_data['Volume'].shift(1)
    stock_data.dropna(inplace=True)
    return stock_data

# Function to predict for the past 7 days
def predict_for_past_7_days(ticker):
    company_data = get_company_data(ticker)
    predictions = []

    # Get the last available row of data
    last_row = company_data.iloc[-1].copy()
    last_date = last_row.name

    # Generate dates for the past 7 business days
    past_7_days = pd.date_range(end=last_date, periods=7, freq='B')[::-1]
    
    for prediction_date in past_7_days:
        # Predict price for the date
        predicted_price = model.predict([[last_row['SMA_10'], last_row['SMA_50'], last_row['RSI'], last_row['Volume_Lag1'], last_row['y_lag1']]])[0]
        
        # Store the prediction
        predictions.append({
            'Company': ticker,
            'Date': prediction_date,
            'Predicted_Price': predicted_price
        })

        # Update features for the next prediction
        last_row['y_lag1'] = predicted_price
        last_row['Volume_Lag1'] = last_row['Volume']  # Assume constant volume
        
        # Update SMA and RSI with the predicted value
        new_close_series = pd.concat([company_data['Close'], pd.Series([predicted_price])], ignore_index=True)
        last_row['SMA_10'] = new_close_series.rolling(window=10).mean().iloc[-1]
        last_row['SMA_50'] = new_close_series.rolling(window=50).mean().iloc[-1]
        last_row['RSI'] = RSIIndicator(new_close_series).rsi().iloc[-1]

    return pd.DataFrame(predictions)

# List of companies
companies = ['AAPL', 'MSFT', 'GOOGL', 'META', 'NVDA', 'AMZN', 'TSLA', 'PYPL', 
    'INTC', 'CSCO']

# Combine predictions for all companies
pred = pd.concat([predict_for_past_7_days(company) for company in companies], ignore_index=True)

import yfinance as yf
import pandas as pd
import datetime

# List of ticker symbols for top 10 NASDAQ-100 companies (example)
tickers = [
    'AAPL', 'MSFT', 'GOOGL', 'META', 'NVDA', 'AMZN', 'TSLA', 'PYPL', 
    'INTC', 'CSCO']

data = yf.download(tickers, period='5d', group_by='ticker')

# Reshape the data to company-wise format
reshaped_data = {}

# Loop through each ticker and organize data company-wise
for ticker in tickers:
    # Select the relevant columns for each company (Open, Close, High, Low, Volume)
    company_data = data[ticker][[ 'Close']]
    company_data['Company'] = ticker  # Add the company ticker as a column for reference
    reshaped_data[ticker] = company_data

# Combine all company data into a single DataFrame
stock = pd.concat(reshaped_data, axis=0)

# Reset index to make the date a regular column (useful for Power BI)
stock.reset_index(inplace=True)

# View the final reshaped data
stock.drop("level_0",axis=1,inplace=True)
stock.rename_axis(None, axis=1, inplace=True)
stock["Date"] = stock["Date"].dt.date

# Ensure both Date columns are in datetime format
pred['Date'] = pd.to_datetime(pred['Date'])
stock['Date'] = pd.to_datetime(stock['Date'])

# Merge the two DataFrames
merged_df = pd.merge(pred, stock, on=['Date', 'Company'], how='inner')

# Reorder columns
merged_df = merged_df[['Company', 'Date', 'Predicted_Price', 'Close']]

# Display the result
merged_df


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
# mae = mean_absolute_error(y_test, y_pred)
# print(f"Mean Absolute Error (MAE): {mae}")

# Save the trained model
joblib.dump(model, 'stock_price_predictor_model.pkl')
