import csv  

from matplotlib import pyplot as plt  
from matplotlib.pyplot import scatter

#读取CSV文件数据  
filename='D://newworkspace2//PythonDemo//resource//Book1.csv'  

with open(filename) as f: #打开这个文件，并将结果文件对象存储在f�?  
    reader=csv.reader(f)  #创建�?个阅读器reader  
    dates,highs,lows=[],[],[]      #声明存储日期，最值的列表  
    header_row=next(reader) #返回文件中的下一�? 
    for row in reader:  
        print(reader.line_num);
        print(len(row))
        dates.append(row[0])    #存储日期  
        high=int(row[1])    #将字符串转换为数�?  
        highs.append(high)   #存储温度�?大�??  
        low=int(row[2])  
        lows.append(low)    #存储温度�?小�??  
# #根据数据绘制图形  
fig, ax = plt.subplots()
# ax1 = fig.add_subplot(2,1,1)
# ax2 = fig.add_subplot(2,1,2)
ax.scatter(dates,highs)
# ax2.scatter(dates,lows)
plt.show()

# import csv 
# import numpy as np
# import matplotlib.pyplot as plt
# filename='D://newworkspace2//PythonDemo//resource//Book1.csv'  
# with open(filename) as f: #打开这个文件，并将结果文件对象存储在f�?  
#     reader=csv.reader(f)  #创建�?个阅读器reader  
#     header_row=next(reader) #返回文件中的下一�?  
#     dates,highs,lows=[],[],[]      #声明存储日期，最值的列表  
#     for row in reader:  
#         dates.append(row[0])    #存储日期  
#         high=int(row[1])    #将字符串转换为数�?  
#         highs.append(high)   #存储温度�?大�??  
#         low=int(row[2])  
#         lows.append(low)    #存储温度�?小�??
#  
# print(dates)
# print(highs)       
# plt.scatter(dates, highs)
# plt.show()
