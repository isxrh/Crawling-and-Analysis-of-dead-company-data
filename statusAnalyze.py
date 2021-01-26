# -*- coding:utf-8 -*-
# 公司融资状态分析,生成饼图

import csv
from pandas import DataFrame
from pyecharts.charts import Pie


def readfile():
    '''
    文件内容存到列表
    :return company_data二维列表
    '''
    company_data = []
    with open('./datas/20年第四季度.csv', 'r') as f:
        file_content = csv.reader(f)
        for row in file_content:
            company_data.append(row)
    return company_data


def statusAnalyze():
    '''
    功能：统计不同融资状态对应的公司数，画饼状图
    '''
    company_data = readfile()
    company_name = [company_data[i][0] for i in range(len(company_data))]
    company_status = [company_data[i][6] for i in range(len(company_data))]
    status_df = DataFrame([company_name, company_status]).transpose()
    status_df.columns = ['company_name', 'status']
    # print(status_df)

    status = status_df.groupby(status_df["status"]).count().sort_values(by=["company_name"], ascending = False)

    x_data = ["尚未获投", "战略投资", "A轮", "B轮", "C轮", "D轮", "天使轮", "不明确"]
    y_data = [int(status["company_name"][i]) for i in x_data]

    # 画饼图
    pie = (
        Pie()
        .add("", [list(z) for z in zip(x_data, y_data)])
        .render("./html/statusPieChart_20.html")
    )


if __name__ == "__main__":
    statusAnalyze()
