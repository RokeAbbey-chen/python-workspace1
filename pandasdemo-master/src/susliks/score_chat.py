import csv  

from matplotlib import pyplot as plt  
from matplotlib.pyplot import scatter

#读取CSV文件数据  
filename='D://newworkspace2//pandasdemo//resource//workbook.csv'  
with open(filename) as f: #打开这个文件，并将结果文件对象存储在f�?  
    reader=csv.reader(f)  #创建�?个阅读器reader  
    header_row=next(reader) #返回文件中的下一�?  
    dates,highs,lows=[],[],[]      #声明存储日期，最值的列表  
    i = 0
    j = 0
    for row in reader:
        line = reader.line_num
        if line ==3928:
            for column in row:
                if  column != '' and int(column) != 0 and j>2 :
                    dates.append(i)    #存储日期  
                    highs.append(int(column))   #存储温度�?大�??  
                    i=i+1
                j=j+1    
# #根据数据绘制图形 散点�? 
print(dates)
print(highs)
# fig, ax = plt.subplots()
# # ax1 = fig.add_subplot(2,1,1)
# # ax2 = fig.add_subplot(2,1,2)
# ax.scatter(dates,highs)
# # ax2.scatter(dates,lows)
# plt.show()
plt.ylim(0, 2000)  # 限定纵轴的范�?
plt.plot(dates,highs,label='Frist line',linewidth=3,color='r',marker='o', 
markerfacecolor='blue',markersize=12) 
plt.legend()  # 让图例生�?
plt.show()