from pyparsing import Token

import Trade_Strategy
import pandas as pd
import Convert_TRY
pd.options.mode.chained_assignment = None  # default='warn'

dict_of_select=Trade_Strategy.dict_of_select

#Convert TRY
XAU_TRY=Convert_TRY.XAU_TRY
EUR_TRY=Convert_TRY.EUR_TRY
GBP_TRY=Convert_TRY.GBP_TRY

path = "USD_TRY Historical Data.csv"
USD_TRY = pd.read_csv(path)
USD_TRY = Trade_Strategy.reverse_data(USD_TRY)
TDNO=int(input("Lütfen işlem Yapmak istediğiniz toplam data sayısını girin(max 1305):"))
liste1 = Trade_Strategy.get_prices(XAU_TRY, TDNO)
liste2 = Trade_Strategy.get_prices(EUR_TRY, TDNO)
liste3 = Trade_Strategy.get_prices(GBP_TRY, TDNO)
liste4 = Trade_Strategy.get_prices(USD_TRY, TDNO)


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
#last step
takip_edilen_path_indexleri=[]
Finish=False
selection_count=2
column = Total_Data["Sell_on_day"]
max_Sell_on_day = column.max()
Trade_Strategy.change_type(Total_Data)

while(Finish==False):
  index_max_prft=Trade_Strategy.find_max_profit_in_selection_index(Total_Data,dict_of_select)# en karlı olanın indexini buluyor
  takip_edilen_path_indexleri.append(index_max_prft)
  value_sell_on_day_index=Total_Data.loc[index_max_prft,"Sell_on_day"] #burada en karlı gelen seçimin satım gününü buluyrouz
  onumde_baslangic_kaldimi=Total_Data.loc[Total_Data["Buy_on_day"]>value_sell_on_day_index].values
  Empty = False
  if onumde_baslangic_kaldimi.size == 0:
      Empty = True
  if(Empty ==True):
    Finish=True
  else:
    value_sell_on_day_index+=1
    dict_of_select=Trade_Strategy.select_and_create_dict(dict_of_select,Total_Data,selection_count,buy_day=value_sell_on_day_index)
    selection_count+=1

print(dict_of_select)
print("***********************")
Path_Of_Trade_DF=Total_Data.loc[takip_edilen_path_indexleri,["Parity","Buy_on_day","Sell_on_day","Profit_in_Trade"]]
Path_Of_Trade_DF.reset_index(drop=True,inplace=True)
Path_Of_Trade_DF.to_csv("Path_Of_Trade_DF.csv")
print(Path_Of_Trade_DF.info())
