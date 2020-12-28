
import requests
import json
import xlwt


def get_data():
    content = requests.get('https://view.inews.qq.com/g2/getOnsInfo?name=disease_foreign')
    # print(content.text)
    # print(type(content.text))
    foreign_list_dict = json.loads(json.loads(content.text)['data'])['foreignList']
    return foreign_list_dict


def save_data_to_excel():
    data_l = get_data()
    # print(data_l)
    print(type(data_l))

    # 创建一个workbook 设置编码
    workbook = xlwt.Workbook(encoding='utf-8')
    # 创建一个worksheet
    worksheet = workbook.add_sheet('COVID-19')
    worksheet2 = workbook.add_sheet('state')

    # 写入excel
    # 参数对应 行, 列, 值
    index = 0
    for key, value in data_l[0].items():
        # print(key)
        if key == 'children': continue
        worksheet.write(0, index, label=key)
        index = index + 1
    row = 1
    for item in data_l:
            col = 0
            for key, value in item.items():
                # print(value)
                if key == 'children': continue
                worksheet.write(row, col, label=value)
                col = col + 1
            row = row + 1

    for item in data_l:
        print(item['children'])
        # for state in item:
        #     pass
            # print(state)

    # 保存
    # workbook.save('../files/Excel_test.xls')


save_data_to_excel()

