import pandas as pd
from spiders import spiderForSchool

dl = pd.read_csv('files/school.csv', encoding='utf-8', usecols=[1,3])
datas = dl.values.tolist()
# print(datas)
# print(datas.head())# 读取前5行
list_addr = []
list_bCount =[]
list_jCount = []
for i in datas:
    if list_addr.__contains__(i[0]):
        pass
    else:
        list_addr.append(i[0])

print(list_addr)

for i in list_addr:
    bNum = 0
    jNum = 0
    for item in datas:
        if item[0] == i:
            if item[1] == '本科':
                bNum += 1
            if item[1] =='高职专科':
                jNum += 1

    list_bCount.append(bNum)
    list_jCount.append(jNum)

print(list_bCount)
print(list_jCount)

for i in range(len(list_addr)-2):
    spiderForSchool.saveToCSV([list_addr[i], list_bCount[i], list_jCount[i]], 'files/filtered_school.csv')







