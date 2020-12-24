
import requests
import json


def get_data():
    content = requests.get('https://view.inews.qq.com/g2/getOnsInfo?name=disease_foreign')
    # print(content.text)
    # print(type(content.text))
    foreign_list_dict = json.loads(json.loads(content.text)['data'])['foreignList']
    return foreign_list_dict


def save_data_to_excel():
    data_l = get_data()
    print(data_l)


save_data_to_excel()

