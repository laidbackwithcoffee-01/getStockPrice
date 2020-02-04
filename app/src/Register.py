# -*- coding: utf-8 -*-

import MySQLdb as db
import utils.getEnvValue as env


class register:

    def __init__(self, df=None):
        self.__df = df
        self.__dbs = env.getmysqlsetting()
        self.__con = db.connect(**self.__dbs)
        self.__cur = self.__con.cursor()

    def check_exists(self, stockName, stockDate):
        self.__cur.execute(
            """
            select *
            from stock_info
            where stock_name = %s and stock_date = %s
            """,
            (stockName, stockDate))
        if self.__cur.rowcount == 0:
            return False
        else:
            return True

    def buld_regist(self, stockName="", df=None):
        if df is not None:
            self.__df = df

        tuples = []
        for index, item in self.__df.iterrows():
            tuples.append(
                (stockName, index, item['High'], item['Low'], item['Open'],
                 item['Close'], item['Volume'], item['Adj Close'])
            )

        self.__cur.executemany(
            "insert into stock_info values(%s, %s, %s, %s, %s, %s, %s, %s)",
            tuples)

        self.__con.commit()

    def regist(self, stockName="", df=None):
        if df is not None:
            self.__df = df

        for index, item in self.__df.iterrows():
            if (not self.check_exists(stockName, index)):
                tuple = (stockName, index, item['High'], item['Low'],
                         item['Open'], item['Close'], item['Volume'],
                         item['Adj Close'])
                self.__cur.execute(
                    """
                    insert into
                    stock_info values(%s, %s, %s, %s, %s, %s, %s, %s)
                    """,
                    tuple)

        self.__con.commit()

    def close(self):
        self.__con.close()
