import json
import quandl


class CommoditiesDataProvider():

    def __init__(self, commodities, date_range):
        with open('SETTINGS.json') as f:
            settings = json.load(f)

        self.API_KEY = str(settings['API_KEY_QUANDL'])
        quandl.ApiConfig.api_key = self.API_KEY

        self.date_range = [date_range[0].strftime("%Y-%m-%d"), date_range[1].strftime("%Y-%m-%d")]
        self.commodities = []
        self.price_data = []

        for commodity in commodities:
            self.add_commodity(commodity)

    def add_commodity(self, commodity):
        self.commodities.append(commodity)
        self.price_data.append(self.__get_data(commodity))

    def __get_data(self, commo):
        start = self.date_range[0]
        end = self.date_range[1]

        s = "Reading %s data, from %s to %s" %(commo, start, end)
        print(s)
        cmm_data = quandl.get(commo, api_key=self.API_KEY, start_date=self.date_range[0], end_date=self.date_range[1])
        return cmm_data

    # def get_data_by_name(self, commodity_name, date_range):
    #
    #     return quandl.get(commodity_name, api_key=self.API_KEY,  start_date=date_range[0], end_date=date_range[1])
