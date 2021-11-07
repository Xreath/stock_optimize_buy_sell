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

path = "USD_TRY Historical Data.csv"
USD_TRY = pd.read_csv(path)
USD_TRY = USD_TRY_Trade.reverse_data(USD_TRY)


XAU_TRY=USD_TRY_Trade.Convert_Data_For_TRY(XAU_USD,USD_TRY)
XAU_TRY.head()