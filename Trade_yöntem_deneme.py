import USD_TRY_Trade
import pandas as pd


path1="XAU_USD Historical Data.csv"
XAU_USD = pd.read_csv(path1)
XAU_USD = USD_TRY_Trade.reverse_data(XAU_USD)
USD_TRY_Trade.Change_Type_XAU_USD(XAU_USD)

path2="EUR_USD Historical Data.csv"
EUR_USD = pd.read_csv(path2)
EUR_USD = USD_TRY_Trade.reverse_data(EUR_USD)

path3="GBP_USD Historical Data.csv"
GBP_USD = pd.read_csv(path3)
GBP_USD = USD_TRY_Trade.reverse_data(GBP_USD)



liste1 = USD_TRY_Trade.get_prices(XAU_USD, 270)
liste2 = USD_TRY_Trade.get_prices(EUR_USD, 270)
liste3 = USD_TRY_Trade.get_prices(GBP_USD, 270)

data=[liste1,liste2,liste3]
data1=[XAU_USD,EUR_USD,GBP_USD]
path=[path1,path2,path3]

x=0
for i,k,j in zip(data,data1,path):
    n = len(i)
    USD_TRY_Trade.stockBuySell(price=i,n=n,money=(1e5 / 3.20),data=k,data_path=j)
    print("##########################################FINAAAL##########################################")


#i want to find nov7-dec2 XAU/TRY
import pandas

