import pandas as pd
from pandas_datareader import data as web
from pandas_datareader._utils import RemoteDataError

import datetime

class SharesConnector():
    company = None
    def __init__(self, center, authentication, company = None):
        self.center = center
        self.authentication = authentication
        self.company = company
        if company != None:
            try:
                cmp_data = web.DataReader(company, self.center, start, end, retry_count=10)
            except RemoteDataError:
                print("%s data is not available at this moment" % comp)
            return cmp_data

    def get_data(self, date_range, comp):
        start = date_range[0]
        end = date_range[1]

        s = "Reading %s data, from %s to %s" %(comp, start, end)
        print(s)
        cmp_data = None
        try:
            cmp_data = web.DataReader(comp, self.center, start, end, retry_count=10)
        except RemoteDataError:
            print("%s data is not available at this moment" %comp)
        return cmp_data

