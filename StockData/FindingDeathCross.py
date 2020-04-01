
# https://pypi.org/project/yfinance/
# Install yfinance package.
#!pip install yfinance
 
# Import yfinance
import fix_yahoo_finance as yf  
import datetime

end = datetime.datetime.now()
start = datetime.datetime.now() - datetime.timedelta(days=1*365)
print(end)
print(start)
 
# Get the data for the stock Apple by specifying the stock ticker, start date, and end date
data = yf.download('DE',start=start,end=end)
rolling_mean = data.rolling(window=200).mean()
rolling_mean2 = data.rolling(window=50).mean()
print((rolling_mean))
print(rolling_mean2)
print(data)
# Plot the close prices
import matplotlib.pyplot as plt
data.Close.plot()
# plt.show()
################ to continue plotting on this https://towardsdatascience.com/implementing-moving-averages-in-python-1ad28e636f9d