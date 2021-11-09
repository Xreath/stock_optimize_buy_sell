import pandas as pd
import Trade_Strategy
from datetime import date,datetime
import pandas
import numpy as np
NaN = np.nan


def Find_total_money_and(data):
    data["Total_Money"]=NaN
    total_days=0
    count = data["Profit_in_Trade"].count()
    main_money = 1e5
    for i in range(0,count):
        profit_ones=data.loc[i,"Profit_in_Trade"]
        ana_paradan_kar = (main_money * profit_ones) / 100
        komisyon_buy = main_money / 500
        komisyon_sell = (main_money + ana_paradan_kar) / 500
        komisyon = komisyon_buy + komisyon_sell

        main_money += ana_paradan_kar - komisyon

        # buy=data.loc[i,"Buy_on_day"]
        # sell=data.loc[i,"Sell_on_day"]
        #
        # Date_Buy = data.loc[buy, ["Date"]].iat[0]
        # Date_Sell = data.loc[sell, ["Date"]].iat[0]
        # main_money += ana_paradan_kar - komisyon
        # d0 = Date_Buy.strip().split()
        # d1 = Date_Sell.strip().split()
        #
        # d0, d1 = Trade_Strategy.clear_date(d0, d1)
        #
        # d0 = date(int(d0[2]), Trade_Strategy.Months.get(d0[0]), int(d0[1]))
        # d1 = date(int(d1[2]), Trade_Strategy.Months.get(d1[0]), int(d1[1]))
        # delta = d1 - d0
        # total_days += delta.days
        data.loc[i, "Total_Money"]=main_money
path="Path_Of_Trade_DF.csv"
DF=pd.read_csv(path)
Find_total_money_and(DF)
DF.to_excel("Path_Of_Trade_DF.xlsx")


