# -*- coding: utf-8 -*-

import os
import csv
import GetStockInfo
import Register

if __name__ == "__main__":
    '''
    NASDAQの株価を取得しDBに保存
    '''
    getStockInfo = GetStockInfo.getStockPrice()
    register = Register.register()

    tsvFilePath = os.path.dirname(
        os.path.abspath(__file__)) + '/env/stocklist.tsv'
    with open(tsvFilePath, newline="") as f:
        reader = csv.DictReader(f, delimiter='\t')
        index = 1
        for row in reader:
            symbol = row['Symbol']
            print('*** starting import stock info No.{} {} ***'.
                  format(index, symbol))
            try:
                df = getStockInfo.getDataFrame(symbol, 2)
                register.regist(symbol, df)
            except Exception as e:
                print(
                    '*** failure import stock info No. {} {} ***'.
                    format(index, symbol))
                print(e)
            index += 1
