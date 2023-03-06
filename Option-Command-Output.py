import math
from scipy.stats import norm
from datetime import datetime, date
import pandas as pd
import yfinance as yf

"""
Enter the ticker, type of option, the strike price, the date 
The system will output the price of an option
"""


def d1(S, K, T, r, sigma):
    return (math.log(S / K) + (r + 0.5 * sigma ** 2) * T) / (sigma * math.sqrt(T))


def d2(S, K, T, r, sigma):
    return d1(S, K, T, r, sigma) - sigma * math.sqrt(T)


# Call option formula
def bs_call(S, K, T, r, sigma):
    return S * norm.cdf(d1(S, K, T, r, sigma)) - K * math.exp(-r * T) * norm.cdf(d2(S, K, T, r, sigma))


def bs_put(S, K, T, r, sigma):
    return K * exp(-r * T) - S + bs_call(S, K, T, r, sigma)


stock = str(input("Select the stock you want: "))
choice = input("Is it a call or a put ? (c/p): ")
expiry = str(input("What is the expiration date (format mm-dd-YYYY): "))
strike_price = int(input("What is the strike price: "))

# Use datetime module to calculate today date and one year ago from today
today = datetime.now()
one_year_ago = today.replace(year=today.year - 1)

# Download the stock price
df = yf.download(stock, start=one_year_ago, end=today)

# Calculate return as it's one of the input of the formula
df = df.sort_values(by="Date")
df = df.dropna()
df = df.assign(close_day_before=df.Close.shift(1))
df["returns"] = (df.Close - df.close_day_before) / df.close_day_before

# Annualized volatility
sigma = np.sqrt(252) * df["returns"].std()

# We use the US Treasury Yield 10 Years as the risk-free interest rate
ty10y = yf.download('^TNX', start=one_year_ago, end=today)["Adj Close"].iloc[-1]

# The current price of the stock
last_close = df["Close"].iloc[-1]

# Time to expiration
t = (datetime.utcnow() - datetime.strptime(expiry, "%m-%d-%Y")).days / 365

if choice == "c":
    print("The Call Price is: ", bs_call(last_close, strike_price, t, ty10y, sigma))

if choice == "p":
    print("The Put Price is: ", bs_put(last_close, strike_price, t, ty10y, sigma))