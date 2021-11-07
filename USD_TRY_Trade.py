# @title USD_TRT Paritesi Tam Kod
import pandas as pd
import numpy as np
import sys
import os
import matplotlib.pyplot as plt
from datetime import date


def reverse_data(data):
    data = data.loc[::-1]
    data = data.reset_index(drop=True)
    return data


def get_prices(data, number=1303):
    Array = data.loc[:number, ["Price"]].values
    list1 = Array.tolist()
    liste = []
    for i in list1:
        liste.extend(i)
    return liste


def Change_Type_XAU_USD(data):
    for col_r in range(1, len(data.columns) - 1):
        clm = data.columns[col_r]
        for k, i in enumerate(data[clm]):
            indexing = i.find('.')
            i = i[:indexing]
            data.loc[k,clm] = i

        data[clm] = [i.replace(",", ".") for i in data[clm]]
        data[clm] = data[clm].astype('float')


def clear_date(d0, d1):
    if (d0[1][0] == "0"):
        d0[1] = d0[1].strip("0,")

    if (d0[1][0] != "0"):
        d0[1] = d0[1].strip(",")

    if (d1[1][0] == "0"):
        d1[1] = d1[1].strip("0,")

    if (d1[1][0] != "0"):
        d1[1] = d1[1].strip(",")
    return d0, d1


def stockBuySell(price, n, money, data, data_path):
    Months = {"Jan": 1, "Feb": 2, "Mar": 3, "Apr": 4, "May": 5, "Jun": 6, "Jul": 7, "Aug": 8, "Sep": 9, "Oct": 10,
              "Nov": 11, "Dec": 12}

    profit_sum = 0
    total_days = 0
    parity_name = data_path.split(" ")[0]
    if(parity_name=="USD_TRY"):
        parity_sym="₺"
    else:
        parity_sym = "$"
    # Prices must be given for at least two days
    if (n == 1):
        return
    # Traverse through given price array
    i = 0
    while (i < (n - 1)):
        # Find Local Minima
        # Note that the limit is (n-2) as we are
        # comparing present element to the next element
        while ((i < (n - 1)) and
               (price[i + 1] <= price[i])):
            i += 1
        # If we reached the end, break
        # as no further solution possible
        if (i == n - 1):
            break
        # Store the index of minima
        buy = i
        i += 1
        # Find Local Maxima
        # Note that the limit is (n-1) as we are
        # comparing to previous element
        while ((i < n) and (price[i] >= price[i - 1])):
            i += 1
        # Store the index of maxima
        sell = i - 1

        kar_yüzde = ((price[sell] - price[buy]) / price[buy]) * 100
        ana_paradan_kar = (money * kar_yüzde) / 100
        komisyon = money / 500

        #profit_sum += ana_paradan_kar

        if (ana_paradan_kar > komisyon):
            Date_Buy = data.loc[buy, ["Date"]].iat[0]
            Date_Sell = data.loc[sell, ["Date"]].iat[0]
            print("Buy on day: ", Date_Buy, "\t", "Sell on day: ",Date_Sell)
            money += ana_paradan_kar - komisyon
            print(f"Profit amount with fee:{int(ana_paradan_kar - komisyon)}{parity_sym}   Total money:{int(money)}{parity_sym}")
            d0 = Date_Buy.strip().split()
            d1 = Date_Sell.strip().split()

            d0, d1 = clear_date(d0, d1)

            d0 = date(int(d0[2]), Months.get(d0[0]), int(d0[1]))
            d1 = date(int(d1[2]), Months.get(d1[0]), int(d1[1]))
            delta = d1 - d0
            total_days += delta.days
            print("Kar yüzdesi",kar_yüzde) #silinecek bu burada kalmasın !!!!!!!!!!!!!!!!!!!!!!
            print(f"******************** Total {parity_name} Days: {total_days} ********************")



if __name__=="__main__":

    path = "USD_TRY Historical Data.csv"
    df = pd.read_csv(path)
    df = reverse_data(df)

    liste = get_prices(df, 200)
    if (path.split(" ")[0] == "USD_TRY"):
        Main_Money = 1e5
    else:
        Main_Money = 1e5 / 3.20

    n = len(liste)
    stockBuySell(price=liste, n=n, money=Main_Money, data=df, data_path=path)