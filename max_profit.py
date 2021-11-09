import Trade_Strategy
import pandas as pd
import Convert_TRY

#Convert TRY
XAU_TRY=Convert_TRY.XAU_TRY
EUR_TRY=Convert_TRY.EUR_TRY
GBP_TRY=Convert_TRY.GBP_TRY

path = "USD_TRY Historical Data.csv"
USD_TRY = pd.read_csv(path)
USD_TRY = Trade_Strategy.reverse_data(USD_TRY)


liste1 = Trade_Strategy.get_prices(XAU_TRY, 14)
liste2 = Trade_Strategy.get_prices(EUR_TRY, 14)
liste3 = Trade_Strategy.get_prices(GBP_TRY, 14)
liste4 = Trade_Strategy.get_prices(USD_TRY, 14)

data=[liste1,liste2,liste3,liste4]
data1=[XAU_TRY,EUR_TRY,GBP_TRY,USD_TRY]
data_name=["XAU_TRY","EUR_TRY","GBP_TRY","USD_TRY"]

for i,k,j in zip(data,data1,data_name):
    n = len(i)
    Trade_Strategy.stockBuySell(price=i,n=n,money=1e5,data=k,Data_Name=j)
    print("##########################################FINAAAL##########################################")

