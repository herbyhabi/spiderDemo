import json

import requests
import time
import execjs


def getUrl(fs_code):
    head = 'http://fund.eastmoney.com/pingzhongdata/'
    tail = '.js?v=' + time.strftime("%Y%m%d%H%M%S", time.localtime())
    return head + fs_code + tail


def formatDate(time_stamp):
    # 转换为其他日期格式,如:"%Y-%m-%d %H:%M:%S"
    timeArray = time.localtime(time_stamp)
    otherStyleTime = time.strftime("%Y-%m-%d", timeArray)
    return otherStyleTime


# 获取净值
def getWorth(fscode):
    # 用requests获取到对应的文件
    content = requests.get(getUrl(fscode))
    print(getUrl(fscode))

    # 使用execjs获取到相应的数据
    jsContent = execjs.compile(content.text)

    print(content.text)
    name = jsContent.eval('fS_name')
    code = jsContent.eval('fS_code')

    # 单位净值走势
    netWorthTrend = jsContent.eval('Data_netWorthTrend')
    print(netWorthTrend)
    # 累计净值走势
    ACWorthTrend = jsContent.eval('Data_ACWorthTrend')
    # print(len(ACWorthTrend))
    fund_data = {}
    ACWorth = []
    worth = []

    list_data = []
    for i in netWorthTrend:
        dic_d_data = {
            "name": name,
            "code": code
        }

        date = formatDate(i["x"]/1000)

        dic_d_data.update({"date": date})
        dic_d_data.update({"net_worth": i["y"]})
        dic_d_data.update({"equity——return": i["equityReturn"]})
        list_data.append(dic_d_data)

    return list_data



fund_list = {'005827','003069', '161726', '160225','110011', '006098', '005224','001593', '001595', '519674', '320007','161005', '110022', '008282', '008087'}
funds = {'005827','110011'}


# net_worth_list = getWorth('005827')
# print(fund_data)

all_list = []
for i in funds:
    single_fund_data_list = getWorth(i)
    print(single_fund_data_list)
    all_list = all_list + single_fund_data_list
# print(net_worth_list)

file_name = '../files/fund_info.json'


with open(file_name, 'a') as file:
    json.dump(all_list, file)

print(formatDate(1536076800))
