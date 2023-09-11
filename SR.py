import subprocess
import yfinance as yf

levels_set_for_day = False
threshold_percentage = 0.005
interval = 30



def set_support_resistance_levels(ticker):
    global interval

    data = ticker.history(period="1d")
    current_price = data['Close'].iloc[-1]
    
    support_level_1 = round(current_price - 2 * (current_price - data['Low'].iloc[-1]), 2)
    support_level_2 = round(current_price - (current_price - data['Low'].iloc[-1]), 2)
    resistance_level_1 = round(current_price + (data['High'].iloc[-1] - current_price), 2)
    resistance_level_2 = round(current_price + 2 * (data['High'].iloc[-1] - current_price), 2)
    
    return support_level_1, support_level_2, resistance_level_1, resistance_level_2



def check_support_proximity(ticker, levels, threshold_percentage):
    data = ticker.history(period="1d")
    current_price = round(data['Close'].iloc[-1], 2)
    
    support_level_1, support_level_2 = levels
    
    if (abs(current_price - support_level_1) / support_level_1 <= threshold_percentage or abs(current_price - support_level_2) / support_level_2 <= threshold_percentage):
        interval = 15
        title = "Close to Support Level"
        message = f"Current Price: {current_price}\nSupport 1: {support_level_1}"
        subprocess.run(['osascript', '-e', f'display notification "{message}" with title "{title}"', '-e', 'delay 10'])

    else:
        interval = 30



def check_resistance_proximity(ticker, levels, threshold_percentage):
    data = ticker.history(period="1d")
    current_price = round(data['Close'].iloc[-1], 2)
    
    resistance_level_1, resistance_level_2 = levels
    
    if (abs(current_price - resistance_level_1) / resistance_level_1 <= threshold_percentage or abs(current_price - resistance_level_2) / resistance_level_2 <= threshold_percentage):
        interval = 15
        title = "Close to Resistance Level"
        message = f"Current Price: {current_price}\nResistance 1: {resistance_level_1}"
        subprocess.run(['osascript', '-e', f'display notification "{message}" with title "{title}"', '-e', 'delay 10'])

    else:
        interval = 30