import Trade_Strategy
import pandas as pd

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



XAU_TRY=Trade_Strategy.Convert_Data_For_TRY(XAU_USD,USD_TRY)
EUR_TRY=Trade_Strategy.Convert_Data_For_TRY(EUR_USD,USD_TRY)
GBP_TRY=Trade_Strategy.Convert_Data_For_TRY(GBP_USD,USD_TRY)

