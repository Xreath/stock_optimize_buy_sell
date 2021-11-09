from pyparsing import Token

import Trade_Strategy
import pandas as pd
import Convert_TRY
pd.options.mode.chained_assignment = None  # default='warn'

#Convert TRY
XAU_TRY=Convert_TRY.XAU_TRY
EUR_TRY=Convert_TRY.EUR_TRY
GBP_TRY=Convert_TRY.GBP_TRY

path = "USD_TRY Historical Data.csv"
USD_TRY = pd.read_csv(path)
USD_TRY = Trade_Strategy.reverse_data(USD_TRY)


liste1 = Trade_Strategy.get_prices(XAU_TRY, 35)
liste2 = Trade_Strategy.get_prices(EUR_TRY, 35)
liste3 = Trade_Strategy.get_prices(GBP_TRY, 35)
liste4 = Trade_Strategy.get_prices(USD_TRY, 35)


data=[liste1,liste2,liste3,liste4]
data1=[XAU_TRY,EUR_TRY,GBP_TRY,USD_TRY]
data_name=["XAU_TRY","EUR_TRY","GBP_TRY","USD_TRY"]


Dataframe_Listesi=[]

for i,k,j in zip(data,data1,data_name):
    n = len(i)
    df=Trade_Strategy.stockBuySell(price=i,n=n,money=1e5,data=k,Data_Name=j)
    Dataframe_Listesi.append(df)
    print("##########################################FINAAAL##########################################")

Total_Data=pd.concat(Dataframe_Listesi)

Total_Data = Total_Data.reset_index(drop=True)
Total_Data.to_excel("excel.xlsx")
SAM=Trade_Strategy.Find_same_trade_index(Total_Data)
Trade_Strategy.Select_High_Profit_Same_Day(Total_Data,SAM)
Total_Data.reset_index(drop=True,inplace=True)
Total_Data.to_excel("excel_after_select.xlsx")
#Reset Trade Index and Index
A,liste_trade_number_sifirla=Trade_Strategy.Reset_Trade_Number_And_Index(Total_Data)
for i in range(len(liste_trade_number_sifirla)):
  liste_trade_number_sifirla[i].Trade_Number=A[i]
Total_Data=pd.concat(liste_trade_number_sifirla,axis=0)
Total_Data.to_excel("excel_after_select1.xlsx")
dict_of_select=Trade_Strategy.select_and_create_dict(Trade_Strategy.dict_of_select,Total_Data,2,buy_day=1)


