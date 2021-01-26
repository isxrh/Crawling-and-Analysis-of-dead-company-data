# -*- coding:utf-8 -*-
# 查询产业对应的有哪些公司
import csv

def findCompany():
    '''
    文件内容存到列表
    :return company_data二维列表
    '''
    company_data = []
    dic = {}
    with open('deadCompany.csv', 'r') as f:
        file_content = csv.reader(f)
        for row in file_content:
            company_data.append(row)

    for i in range(len(company_data)):
        list1 = company_data[i]
        str1 = str(list1[0])
        str2 = str(list1[4])
        dic.update({str1: str2})
    str2 = input()
    list2 = []
    for i, j in dic.items():
        if (j == str2):
            list2.append(i)
    return list2


if __name__ == "__main__":
    findCompany()