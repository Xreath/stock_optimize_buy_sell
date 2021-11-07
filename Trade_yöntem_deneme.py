import USD_TRY_Trade
import pandas as pd


path="XAU_USD Historical Data.csv"
XAU_USD = pd.read_csv(path)
XAU_USD = USD_TRY_Trade.reverse_data(XAU_USD)
USD_TRY_Trade.Change_Type_XAU_USD(XAU_USD)

path="EUR_USD Historical Data.csv"
EUR_USD = pd.read_csv(path)
EUR_USD = USD_TRY_Trade.reverse_data(EUR_USD)

path="GBP_USD Historical Data.csv"
GBP_USD = pd.read_csv(path)
GBP_USD = USD_TRY_Trade.reverse_data(GBP_USD)



liste1 = USD_TRY_Trade.get_prices(XAU_USD, 10)
liste2 = USD_TRY_Trade.get_prices(EUR_USD, 10)
liste3 = USD_TRY_Trade.get_prices(GBP_USD, 10)

data=[liste1,liste2,liste3]
data1=[XAU_USD,EUR_USD,GBP_USD]

x=0
for i,k in zip(data,data1):
    n = len(i)
    USD_TRY_Trade.stockBuySell(price=i,n=n,money=(1e5 / 3.20),data=k,data_path=path)
    print("**************************************FINAAAL************************************************")
