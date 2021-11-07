import Trade_Strategy
import pandas as pd
import Convert_TRY

#Convert TRY
XAU_TRY=Convert_TRY.XAU_TRY
EUR_TRY=Convert_TRY.EUR_TRY
GBP_TRY=Convert_TRY.GBP_TRY




liste1 = Trade_Strategy.get_prices(XAU_TRY, 20)
liste2 = Trade_Strategy.get_prices(EUR_TRY, 20)
liste3 = Trade_Strategy.get_prices(GBP_TRY, 20)

data=[liste1,liste2,liste3]
data1=[XAU_TRY,EUR_TRY,GBP_TRY]
data_name=["XAU_TRY","EUR_TRY","GBP_TRY"]

x=0
for i,k,j in zip(data,data1,data_name):
    n = len(i)
    Trade_Strategy.stockBuySell(price=i,n=n,money=(1e5 / 3.20),data=k,Data_Name=j)
    print("##########################################FINAAAL##########################################")


#i want to find nov7-dec2 XAU/TRY
import pandas

