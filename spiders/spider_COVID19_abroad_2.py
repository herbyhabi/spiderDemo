import requests
import json
import xlwt
from utils import commen_func


def get_data():
    data = dict(
        key='a104d29c02197b89f8eb2dd287d69e12'
    )
    res = requests.get('http://api.tianapi.com/txapi/ncovabroad/index', params=data)

    res_json = json.loads(res.text)

    return res_json


def save_data_to_excel():
    l_covid_data = get_data()['newslist']
    # print(l_covid_data)
    # 创建一个workbook 设置编码
    workbook = xlwt.Workbook(encoding='utf-8')
    # 创建一个worksheet
    worksheet = workbook.add_sheet('COVID19_abroad')

    # 添加表字段名称
    col = 0
    for key in l_covid_data[0].keys():
        worksheet.write(0, col, label=key)
        col = col + 1

    row = 1
    for province in l_covid_data:
        col1 = 0
        for key, value in province.items():
            if key == 'modifyTime':
                print(value)
                new_value = commen_func.funcs.format_date(value/1000)
                print(new_value)
                worksheet.write(row, col1, label=new_value)
            else:
                worksheet.write(row, col1, label=value)
            col1 = col1 + 1
        row = row + 1






    # 保存
    workbook.save('../files/Excel_test.xls')
save_data_to_excel()

