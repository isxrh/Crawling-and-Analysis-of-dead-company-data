# -*- coding:utf-8 -*-
# 公司地区分布分析，生成分布地图
from pyecharts.charts import Map
from functools import cmp_to_key
from pyecharts import options as opts
import csv


def companyTypeMap():
    with open('./datas/20年第四季度.csv', 'r') as csvfile:
        reader = csv.reader(csvfile)
        column = [row[5] for row in reader]
    list2 = sorted(column) #列表排序
    list3 = list(set(column)) #列表去重复
    list4=[]
    list5 = []
    for i in list3:
        j = list2.count(i) #统计字符个数
        list4.append((i, j)) #将字符及个数加入新列表
    def recmp(x, y): #定义一个排序函数与 cmp 函数输出结果相反
        if x < y :
            return 1
        if x == y:
            return 0
        if x > y:
            return -1
    list4.sort(key=cmp_to_key(lambda x,y:recmp(x[1],y[1])))

    map=(
        Map()
        .add("", list4, "china")
        .set_global_opts(
            title_opts=opts.TitleOpts(title="地区分布",pos_right="center",pos_top="5%"),
            visualmap_opts=opts.VisualMapOpts(max_=50),
        )
    )
    map.render("./html/chinaMap_2020.html")


if __name__ == "__main__":
    companyTypeMap()