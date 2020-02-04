# -*- coding: utf-8 -*-

import pandas_datareader.data as pdd
import datetime


class getStockPrice:

    def __init__(self, stockName="", day=0):
        self.stockName = stockName
        self.day = day

    def getDataFrame(self, stockName="", day=0):
        if stockName != "":
            self.stockName = stockName
        if day != 0:
            self.day = day
        if self.stockName == "":
            raise Exception
        today = datetime.date.today()
        return pdd.DataReader(
            self.stockName, 'yahoo', today - datetime.timedelta(days=self.day))
