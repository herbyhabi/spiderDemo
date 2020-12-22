import csv

import requests
import time
import random
import lxml
from lxml import etree


def spider(url):
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/75.0.3770.100 Safari/537.36'}
    response = requests.get(url, headers=headers)
    time.sleep(random.randint(0, 2))  # 同样用于反爬虫
    return etree.HTML(response.text)


def parse(url):
    whole_page = spider(url)
    all_list = whole_page.xpath('//*[starts-with(@class,"scores_List")]/dl')
    # print(all_list)

    for sel in all_list:
        name = sel.xpath('dt/strong/a/text()')[0]
        place = sel.xpath('dd/ul/li[1]/text()')[0][6:]
        s_type = sel.xpath('dd/ul/li[3]/text()')[0][5:]  # 高校类型
        nature = sel.xpath('dd/ul/li[5]/text()')[0][5:]  # 高校性质
        try:
            style = sel.xpath('dd/ul/li[2]/span/text()')[0]
        except:
            style = ''
        saveToCSV([name,place,s_type,nature,style],'../files/school.csv')


def saveToCSV(item, path):
    with open(path, 'a', encoding='utf-8', newline='') as file:
        writer = csv.writer(file)
        try:
            writer.writerow(item)
        except Exception as e:
            print(e)
    file.close()


if __name__ == "__main__":
    url_ = "http://college.gaokao.com/schlist/p"
    all_pages = [url_ + str(i) for i in range(1,3)]
    for url in all_pages:
        print(url)
        parse(url)
