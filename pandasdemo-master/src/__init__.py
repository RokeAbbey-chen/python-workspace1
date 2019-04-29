import pandas
from pandas import DataFrame
import xlrd


data=pandas.read_csv("C://Users//Administrator//Desktop//workbook//111.csv")
df = DataFrame(data)
# print(data)
# print(type(data))
# print(data.dtypes)
# print(data.head(3))
# print(data.tail(3))
# print(data.columns)
# print(data.mean(1))
seq=[1,2,3,4]
ls = [151.0, 154.0]
# print(ls[2:5])
ls = sorted(ls);
lenth = len(ls)
# print(ls[int(lenth*0.5):lenth])
# print(int(sum(ls) / lenth))
sls = pandas.Series(seq);
print(sls.max());
data["means"] = ls;
df.to_csv("C://Users//Administrator//Desktop//workbook//111.csv");