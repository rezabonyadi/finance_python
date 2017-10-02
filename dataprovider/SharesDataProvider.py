import pandas as pd
from pandas_datareader import data as web
from pandas_datareader._utils import RemoteDataError

import datetime

class SharesDataProvider():

    def __init__(self, center, authentication, companies, date_range):
        self.center = center
        self.authentication = authentication
        self.date_range = date_range
        self.companies = []
        self.stock_data = []

        for company in companies:
            self.add_company(company)

    def add_company(self, company):
        self.companies.append(company)
        self.stock_data.append(self.__get_data(company))

    def get_current_data(self):
        return {"Companies": self.companies, "Stock": self.stock_data, "Date_range": self.date_range}

    def get_all_data_by_company(self, comp):
        cmp_indx = [i for i, x in enumerate(self.companies) if x == comp]
        if len(cmp_indx) > 0:
            return self.stock_data[cmp_indx[0]]
        else:
            return None

    def get_adjusted_closing_by_company(self, comp):
        cmp_indx = [i for i, x in enumerate(self.companies) if x == comp]
        if len(cmp_indx) > 0:
            return self.stock_data[cmp_indx[0]]["Adj Close"]
        else:
            return None

    def get_close_by_company(self, comp):
        cmp_indx = [i for i, x in enumerate(self.companies) if x == comp]
        if len(cmp_indx) > 0:
            return self.stock_data[cmp_indx[0]]["Close"]
        else:
            return None

    def get_high_by_company(self, comp):
        cmp_indx = [i for i, x in enumerate(self.companies) if x == comp]
        if len(cmp_indx) > 0:
            return self.stock_data[cmp_indx[0]]["High"]
        else:
            return None

    def get_low_by_company(self, comp):
        cmp_indx = [i for i, x in enumerate(self.companies) if x == comp]
        if len(cmp_indx) > 0:
            return self.stock_data[cmp_indx[0]]["Low"]
        else:
            return None

    def get_open_by_company(self, comp):
        cmp_indx = [i for i, x in enumerate(self.companies) if x == comp]
        if len(cmp_indx) > 0:
            return self.stock_data[cmp_indx[0]]["Open"]
        else:
            return None

    def __get_data(self, comp):
        start = self.date_range[0]
        end = self.date_range[1]

        s = "Reading %s data, from %s to %s" %(comp, start, end)
        print(s)
        cmp_data = None
        try:
            cmp_data = web.DataReader(comp, self.center, start, end, retry_count=10)
        except RemoteDataError:
            print("%s data is not available at this moment" %comp)
        return cmp_data

