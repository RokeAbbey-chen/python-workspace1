'''
Created on 2018年10月25日

@author: Administrator
'''
import pandas
from pandas import DataFrame, Series
import math
import numpy as np
# 
data = pandas.read_csv("./elo_1008.csv")
# print(len(data))
df = DataFrame(data)
means = []
std = []
min = []
max = []
# print(df)
# print(df.ix[[1]].values[0][0])
# print(df.ix[[3]].columns.size)
# print(data.shape[1])
df1 = df.drop(['user_id','elo','number'], axis=1)
for j in range(0, df1.shape[0]):
    columnCount = 0
    rowData = []
    for i in range(0, df1.shape[1]):
        column = df1.ix[[j]].values[0][i]
        if not math.isnan(column) and column > 0:
           rowData.append(column if column >= 0 else -column + 50)
    rowData = sorted(rowData)
    lenth = len(rowData)
    firstlen = int(lenth*0.1)
    rowData = rowData[firstlen:lenth]
    lenth = lenth-firstlen
    rowDataSeries = pandas.Series(rowData)
    # print('rowData = {}'.format(rowData))
    min_m = rowDataSeries.min()
    max_m = rowDataSeries.max()
    if math.isnan(min_m):
        min.append(0)
    else:
        min.append(min_m)
    if math.isnan(max_m):
        max.append(0)
    else:
        max.append(max_m)
    if lenth != 0:
        means.append(int(sum(rowData) / lenth))
        mean = rowDataSeries.std()
        # print("np.std0 = {}, np.std1 = {}, pandas.std = {}".format( np.std(rowData), np.std(rowData, ddof=1), mean))
        if math.isnan(mean):
            std.append(0)
        else:
            std.append(round(mean, 2))
    else:
         means.append(0)
         std.append(0)
print(means)
print(std)
print(len(min))
print(len(max))
data["means"] = means
data["std"] = std
data["min"] = min
data["max"] = max
df.to_csv("./1008_0.1.csv")

# df1 = df.drop(['index','user_id','elo','number'], axis=1)
# for j in range(0, df1.shape[0]):
#     print(df1.mean(j))
#     means.append(df1.mean(j)) 
# df1["means"] = means
# print(df1)    
      
#字典中的key值即为csv中列名
# dataframe = data.DataFrame({'a_name':data["user_id"]/100})
# 
# #将DataFrame存储为csv,index表示是否显示行名，default=True
# dataframe.to_csv(basestation,index=False, mode='a')
# print(data.shape)                  
# df = pandas.DataFrame(data)
# pandas.concat([df, pandas.DataFrame({'a_name':data["user_id"]/100})])
               
# basestation ="C://Users//Administrator//Desktop//workbook//111.xls"
# data = pandas.read_excel(basestation)
# print(data.shape)
# print(data["user_id"])
# data["mean"] = data["user_id"]/100
# print(data.shape)
# df=DataFrame(data)
# print(data)
# print(df.ix[[1]].columns.size)
