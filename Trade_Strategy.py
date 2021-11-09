import pandas as pd
import numpy as np
import sys
import os
import matplotlib.pyplot as plt
from datetime import date,datetime

parity_to_number_dict = {"XAU_TRY": 1, "EUR_TRY": 2, "GBP_TRY": 3, "USD_TRY": 4}
number_to_parity_dict = {1:"XAU_TRY", 2 :"EUR_TRY", 3:"GBP_TRY", 4:"USD_TRY"}
dict_of_select={'Select_1': {1: 0, 2: 0, 3: 0, 4: 0}}


def Repeat(data):
    value_list = []
    Buy_on_day = data.iloc[:, 2]
    Buy_on_day = Buy_on_day.astype("int")

    for i in Buy_on_day:
        value_list.append(i)

    _size = len(value_list)
    repeated = []
    for i in range(_size):
        for j in range(i + 1, _size):
            if value_list[i] == value_list[j] and value_list[i] not in repeated:
                repeated.append(value_list[i])
    return repeated


def Reset_Trade_Number_And_Index(data):
  data.reset_index(drop=True,inplace=True)
  data['Trade_Number']=data['Trade_Number'].astype("int")
  liste_trade_number_sifirla=[]
  A=[]
  for i in parity_to_number_dict.keys():
    liste_trade_number_sifirla.append(data.loc[(data["Parity"] ==i)])

  for sayi,j in enumerate(liste_trade_number_sifirla):
    count=liste_trade_number_sifirla[sayi].count()[3]
    A.append(list(range(0,count)))

  return A,liste_trade_number_sifirla



def select_and_create_dict(dict_slct,df,number_of_selection,buy_day):
    df["Buy_on_day"]=df["Buy_on_day"].astype("int")
    df["Sell_on_day"]=df["Sell_on_day"].astype("int")
    str_value="Select"+"_"+str(number_of_selection)
    dict_ll_selected={}
    idx=df[df["Buy_on_day"] == buy_day].index # same buy day in parity
    for i in idx:
        print(i)
        val_hala=[]
        for j in parity_to_number_dict.keys():
          try:
            val=df.loc[(df["Buy_on_day"] == buy_day) & (df["Parity"] == j)]["Trade_Number"].values[0] #trade number this parity
            val_hala.append(val)
          except IndexError:
            pass
        dict_ll_selected[parity_to_number_dict.get(df["Parity"][i])]=val_hala[0]
    dict_slct[str_value]=dict_ll_selected
    return dict_slct



def Select_High_Profit_Same_Day(data, indexes):
    for i in indexes:
        maxim = 0
        for j in i:
            if (data["Profit_in_Trade"][j] > maxim):
                maxim = data["Profit_in_Trade"][j]
            else:
                pass
        max_val_index = data.index.values[data['Profit_in_Trade'] == maxim][0]

        for elem in i:
            if (elem != max_val_index):
                data.drop(elem, inplace=True)
            else:
                pass


def Find_same_trade_index(data):
    same_trade_index=[]
    Days = data.iloc[:,2:4]
    Days=Days.astype("int")
    boolean=Days.duplicated(keep='last')
    days_value=Days[boolean].values
    for i in days_value:
      same_trade_index.append(Days[(Days["Buy_on_day"]==i[0])  & (Days["Sell_on_day"]==i[1])].index.values.astype(int))

    SAM1 = []
    for i in same_trade_index:
        i = i.tolist()
        SAM1.append(i)

    SAM2 = []
    for elem in SAM1:
        if elem in SAM2:
            pass
        else:
            SAM2.append(elem)

    return SAM2


def Convert_Data_For_TRY(data, data1):
    df = pd.DataFrame()
    for col_r in range(0, len(data.columns) - 1):
        clm = data.columns[col_r]
        if(clm!="Date"):
            for i, (j, k) in enumerate(zip(data[clm].values, data1[clm].values)):
                değer = j * k
                değer = round(değer, 3)
                df.loc[i,clm] = değer
        else:
            df[clm] = data[clm]
    return df



def reverse_data(data):
    data = data.loc[::-1]
    data = data.reset_index(drop=True)
    return data


def get_prices(data, number=1303):
    Array = data.loc[:number-1, ["Price"]].values
    list1 = Array.tolist()
    liste = []
    for i in list1:
        liste.extend(i)
    return liste


def Change_Type_XAU_USD(data):
    for col_r in range(1, len(data.columns) - 1):
        clm = data.columns[col_r]
        for k, i in enumerate(data[clm]):
            m=i.find(",")
            i=i[0:m]+i[m+1:len(i)]
            data.loc[k,clm] = i

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


def stockBuySell(price, n, money, data, Data_Name):
    Months = {"Jan": 1, "Feb": 2, "Mar": 3, "Apr": 4, "May": 5, "Jun": 6, "Jul": 7, "Aug": 8, "Sep": 9, "Oct": 10,
              "Nov": 11, "Dec": 12}

    data_frame=pd.DataFrame(columns=["Trade_Number","Parity","Buy_on_day","Sell_on_day","Profit_amount_with_fee","Total_money","Profit_in_Trade"])
    profit_sum = 0
    total_days = 0
    index=0
    #parity_name = data_path.split(" ")[0]
    # if(parity_name=="USD_TRY"):
    #     parity_sym="₺"
    # else:
    #     parity_sym = "$"

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
        komisyon_buy = money / 500
        komisyon_sell=(money+ana_paradan_kar)/500
        komisyon=komisyon_buy+komisyon_sell


        if (ana_paradan_kar > komisyon):
            Date_Buy = data.loc[buy, ["Date"]].iat[0]
            Date_Sell = data.loc[sell, ["Date"]].iat[0]
            print("Buy on day: ", Date_Buy, "\t", "Sell on day: ",Date_Sell)
            money += ana_paradan_kar - komisyon
            print(f"Profit amount with fee:{int(ana_paradan_kar - komisyon)}Tl   Total money:{int(money)}Tl")
            d0 = Date_Buy.strip().split()
            d1 = Date_Sell.strip().split()

            d0, d1 = clear_date(d0, d1)

            d0 = date(int(d0[2]), Months.get(d0[0]), int(d0[1]))
            d1 = date(int(d1[2]), Months.get(d1[0]), int(d1[1]))
            delta = d1 - d0
            total_days += delta.days
            print("Kar yüzdesi",kar_yüzde) #silinecek bu burada kalmasın !!!!!!!!!!!!!!!!!!!!!!
            print(f"                Total {Data_Name} Days: {total_days}          ")

            data_frame.loc[index,["Trade_Number"]]=index
            data_frame.loc[index,["Parity"]]=Data_Name
            data_frame.loc[index,["Buy_on_day"]]=buy
            data_frame.loc[index,["Sell_on_day"]]=sell
            data_frame.loc[index,["Profit_amount_with_fee"]]=int(ana_paradan_kar - komisyon)
            data_frame.loc[index,["Total_money"]]=int(money)
            data_frame.loc[index,["Profit_in_Trade"]]=round(kar_yüzde,4)
            index+=1

    #data_frame.set_index('Trade_Number')

    return data_frame



if __name__=="__main__":

    path = "USD_TRY Historical Data.csv"
    df = pd.read_csv(path)
    df = reverse_data(df)

    liste = get_prices(df, 30)
    Main_Money = 1e5

    n = len(liste)
    trade_verisi=stockBuySell(price=liste, n=n, money=Main_Money, data=df,Data_Name="USD_TRY")



