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

df1=XAU_USD.iloc[:10,0:2]
df2=EUR_USD.iloc[:10,0:2]
df3=GBP_USD.iloc[:10,0:2]


frames = [df1, df2, df3]

result = pd.concat(frames,axis=1)

print(result)


