import Trade_Strategy
import pandas as pd
import Convert_TRY


path="XAU_USD Historical Data.csv"
XAU_USD = pd.read_csv(path)
XAU_USD = Trade_Strategy.reverse_data(XAU_USD)
Trade_Strategy.Change_Type_XAU_USD(XAU_USD)

path="EUR_USD Historical Data.csv"
EUR_USD = pd.read_csv(path)
EUR_USD = Trade_Strategy.reverse_data(EUR_USD)

path="GBP_USD Historical Data.csv"
GBP_USD = pd.read_csv(path)
GBP_USD = Trade_Strategy.reverse_data(GBP_USD)

path = "USD_TRY Historical Data.csv"
USD_TRY = pd.read_csv(path)
USD_TRY = Trade_Strategy.reverse_data(USD_TRY)

#Convert TRY
EUR_TRY=Convert_TRY.EUR_TRY
GBP_TRY=Convert_TRY.GBP_TRY
XAU_TRY=Convert_TRY.XAU_TRY

XAU_TRY_FR=XAU_TRY.loc[:15-1,["Date","Price"]]
EUR_TRY_FR=EUR_TRY.loc[:15-1,["Date","Price"]]
GBP_TRY_FR=GBP_TRY.loc[:15-1,["Date","Price"]]
USD_TRY_FR=USD_TRY.loc[:15-1,["Date","Price"]]


frames = [XAU_TRY_FR,EUR_TRY_FR,GBP_TRY_FR, USD_TRY_FR]

result = pd.concat(frames,axis=1)

print(result)


