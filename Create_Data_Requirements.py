import pandas as pd
import Trade_Strategy
from datetime import date,datetime
import pandas
import numpy as np
NaN = np.nan
import Trade_Path_Finder


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
        data.loc[i, "Total_Money"]=int(main_money)
    parity_gun_toplam = []  # Sıralı 1.si XAU_TRY
    for i in Trade_Strategy.parity_to_number_dict.keys():
        usd_try_selection = data.loc[data["Parity"] == i]
        usd_try_selection = usd_try_selection.iloc[:, 2:4]
        usd_try_selection = usd_try_selection.diff(axis=1, periods=1)
        array = usd_try_selection.iloc[:, 1].values
        parity_gun_toplam.append(array.sum(axis=0))

    return parity_gun_toplam

path="Sonuç Dataları/Path_Of_Trade_DF.csv"
DF=pd.read_csv(path)
parity_gun_toplam=Find_total_money_and(DF)
print(" XAU_TRY Parity Total Day is:",parity_gun_toplam[0],"\n",
      "EUR_TRY Parity Total Day is:",parity_gun_toplam[1],"\n",
      "GBP_TRY Parity Total Day is:",parity_gun_toplam[2],"\n",
      "USD_TRY Parity Total Day is:",parity_gun_toplam[3])

print(" Maximum Money is Maximum money value:",int(DF["Total_Money"].iloc[-1]))

def Gecis_Bul(data):
  _size=data["Parity"].count()
  degisim_diction = {}
  cnt = 1
  for i in range(_size):
    if(_size-1 != i):
      pointer1 =data.loc[i]["Parity"]
      pointer2= data.loc[i+1]["Parity"]
      if(not pointer2 == pointer1):
        degisim_diction["Gecis_"+str(cnt)]=[pointer1,pointer2,
        Trade_Path_Finder.Data_Days_Index.iloc[data.loc[i]["Sell_on_day"]],
        Trade_Path_Finder.Data_Days_Index.iloc[data.loc[i+1]["Buy_on_day"]]]
        cnt+=1

  return degisim_diction

degisim=Gecis_Bul(DF)
print(degisim)
DF.to_excel("Sonuç Dataları/Path_Of_Trade_DF.xlsx")


