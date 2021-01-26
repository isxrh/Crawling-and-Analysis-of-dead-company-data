# -*- coding:utf-8 -*-
# 公司生存时长分析，生成柱状图

import csv
import re
from pyecharts import options as opts
from pyecharts.charts import Bar
import pandas as pd


def readfile():
    '''
    文件内容存到列表
    :return company_data二维列表
    '''
    company_data = []
    with open('./datas/18年第四季度.csv', 'r') as f:
        file_content = csv.reader(f)
        for row in file_content:
            company_data.append(row)
    return company_data


def liveTimeAnalyze():
    '''
    功能：统计不同生存时长区间的公司数，画出柱状图
    '''
    company_data = readfile()
    # 字符串数据转数字
    live_time = [company_data[i][1] for i in range(len(company_data))]
    live_time = [re.findall(r"\d+\.?\d*", i) for i in live_time]
    # print(live_time)
    live_time_year = [int(i[0]) + int(i[1]) / 12.0 for i in live_time]

    # 数据分段
    bins = [i for i in range(0, 28, 2)]
    year_cut = pd.cut(live_time_year, bins)
    count = pd.value_counts(year_cut).sort_index().to_list()

    # 画柱状图
    xaxis_name = []     # 柱状图每个横坐标名称
    for index in range(0, 20, 2):
        s = "(" + str(index) + "," + str(index + 2) + "]"
        xaxis_name.append(s)
    bar = (
        Bar()
        .add_xaxis(xaxis_name)     # 横坐标
        .add_yaxis('公司生存时长统计个数', count)     # 纵坐标
        .set_global_opts(
            # 图表、横、纵坐标 标题
            title_opts=opts.TitleOpts(title="公司生存时长统计表"),
            yaxis_opts=opts.AxisOpts(name="公司数目"),
            xaxis_opts=opts.AxisOpts(name="生存年数"),
        )
    )
    bar.render("./html/liveTimeHistogram_18.html")


if __name__ == '__main__':
    liveTimeAnalyze()













