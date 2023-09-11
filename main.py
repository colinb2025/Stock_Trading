import yfinance as yf
import time
import datetime
import SR
import SMA


ticker = yf.Ticker("AAPL")


while True:
    current_time = datetime.datetime.now().time()

    if (current_time.hour == 8 and current_time.minute == 0) or not SR.levels_set_for_day:
        support_level_1, support_level_2, resistance_level_1, resistance_level_2 = SR.set_support_resistance_levels(ticker)

    SR.check_support_proximity(ticker, (support_level_1, support_level_2), SR.threshold_percentage)
    SR.check_resistance_proximity(ticker, (resistance_level_1, resistance_level_2), SR.threshold_percentage)

    time.sleep(SR.interval)