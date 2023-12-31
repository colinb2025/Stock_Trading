# Stock Trading Algorithm

# Overview

This WIP project implements a stock trading algorithm using Python and several libraries including YFinance, Pandas, DateTime, and Subprocess. The algorithm continuously monitors stock data and sends notifications based on specific conditions.

# Statistics

 - Achieved roughly 22.1% average return on options trading during the first week of testing.
 - Utilized manual stop-loss levels and manual selling points for the results.

# Key Features

 - Moving Averages (SMA): The algorithm calculates short-term and long-term Simple Moving Averages (SMA) for a given stock.
 - SMA Crossover Signals: When the short-term SMA crosses above or below the long-term SMA, the algorithm generates "Buy" or "Sell" signals respectively.
 - Support and Resistance Levels: The algorithm identifies potential support and resistance levels and sends notifications when the stock price approaches these levels.
 - Notifications: Using the Subprocess library, the algorithm sends desktop notifications to alert the user of trading signals or approaching support/resistance levels.
