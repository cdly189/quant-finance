# Demonstration using Black-Scholes Formula
# Section 3.8 "A Primer Mathematics for Financial Engineering" by Dan Stefanica
# Page 109-110

import numpy as np


# Cumulative standard normal distribution

def cum_dist_normal(t):
    y = 1 / (1 + 0.2316419 * abs(t))
    a1 = 0.319381530
    a2 = -0.356563782
    a3 = 1.781477937
    a4 = -1.821255978
    a5 = 1.330274429
    m = 1 - np.exp(-t ** 2 / 2) * (a1 * y + a2 * y ** 2 + a3 * y ** 3 + a4 * y ** 4 + a5 * y ** 5) / np.sqrt(
        2 * np.pi)

    if t > 0:
        return m
    else:
        return 1 - m


# Black-Scholes Formula
t = 0  # Present time
S = 42  # Spot price of the underlying asset
K = 40  # Option strike
T = 0.5  # maturity date
sigma = 0.3  # volatility of the underlying asset
r = 0.05  # constant interest rate
q = 0.03  # continuous dividend rate of the underlying

# C = price of the European call option
# P = price of the European put option

d1 = ((np.log(S / K)) + (r - q + sigma ** 2 / 2) * (T - t)) / (sigma * np.sqrt(T - t))
d2 = d1 - sigma * np.sqrt(T - t)

C = S * np.exp(-q * (T - t)) * cum_dist_normal(d1) - K * np.exp(-r * (T - t)) * cum_dist_normal(d2)
P = K * np.exp(-r * (T - t)) * cum_dist_normal(-d2) - S * np.exp(-q * (T - t)) * cum_dist_normal(-d1)

print(d1)
print(d2)
print(cum_dist_normal(d1))
print(cum_dist_normal(d2))
print(C)
print(P)
