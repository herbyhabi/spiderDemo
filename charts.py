from pyecharts.charts import Bar
from pyecharts import options as opts
import csv
import pandas as pd
data1 = []
data2 = []
data3 = []

with open('new.csv','r') as file:
    reader = csv.reader(file)
    for i in reader:
        data1.append(i[0])
        data2.append(i[1])
        data3.append(i[2])

print(data1)
x1 = data1# 变成列表形式
y1 = data2
y2 = data3

#	更新后有两种调用方法	不习惯链式调用依旧可以单独调用方法
#	链式调用		V1版本要求>=1.0
bar = (
    Bar()
        .add_xaxis(x1)
        .add_yaxis("本科", y1)
        .add_yaxis("专科", y2)
        .set_global_opts(title_opts=opts.TitleOpts(title="大学", subtitle="情况"))
)
bar.render(path='bar.html')

# 单独调用

bar = Bar()
bar.add_xaxis(x1)
bar.add_yaxis("本科", y1)
bar.add_yaxis("专科", y2)
bar.set_global_opts(title_opts=opts.TitleOpts(title="大学", subtitle="情况"))
bar.render(path='bar.html')
