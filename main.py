from datetime import date
import quandl

import matplotlib.pyplot as plt

from dataprovider.SharesDataProvider import SharesDataProvider as dp
from dataprovider.CommoditiesDataProvider import CommoditiesDataProvider as cp
# import dataprovider.CommoditiesDataProvider as cp

# from yahoo_finance import Currency, Share, Commodity, edt_to_utc, get_date_range

# data = quandl.get("FRED/GDP", start_date="2001-12-31", end_date="2005-12-31", collapse="daily")
# plt.plot(data)
# plt.show()

commodities_bank = cp({"FRED/GDP"}, [date(2016, 1, 1), date(2016, 5, 1)])

plt.figure()

stock_bank = dp("yahoo", "", {"AAPL", "MSFT"}, [date(2016, 1, 1), date(2016, 5, 1)])
xx = stock_bank.get_adjusted_closing_by_company("AAPL")
i = 0

data1 = stock_bank.get_adjusted_closing_by_company("AAPL")
# plt.subplot(211)
plt.plot(data1)
plt.hold

data2 = stock_bank.get_adjusted_closing_by_company("MSFT")
plt.subplot(212)
plt.plot(data2)
plt.show()

# msft_data = my_data_provider.get_data(data_range, "MSFT")
# google_data = my_data_provider.get_data(data_range, "GOOG")
#
# stocks = pd.DataFrame({"AAPL": apple_data["Adj Close"],
#                       "MSFT": msft_data["Adj Close"]})

# with pd.option_context('display.max_rows', None, 'display.max_columns', 3):
#     print(stocks.head(20))


