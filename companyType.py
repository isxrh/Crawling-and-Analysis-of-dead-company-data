# -*- coding:utf-8 -*-
# 公司类型分析，生成词云图
import collections
from pyecharts.charts import WordCloud
import csv


def companyTypeWordCloud():
    with open('./datas/20年第四季度.csv', 'r') as csvfile:
        reader = csv.reader(csvfile)
        column = [row[4] for row in reader]
    object_list = []
    for word in column:  # 循环读出每个分词
        object_list.append(word)
    # print(object_list)
    word_counts = collections.Counter(object_list)  # 对分词做词频统计
    word_counts_top10 = word_counts.most_common(10)  # 获取前10最高频的词
    print(word_counts)  # 输出检查

    word_cloud = WordCloud()
    data = dict(sorted({k: v for k, v in word_counts.items() if len(k) >= 2}.items(), key=lambda x: x[1], reverse=True)[:200])
    print(data)
    word_cloud.add(data.keys(), data.items())
    word_cloud.render('./html/companyType_20.html')


if __name__ == "__main__":
    companyTypeWordCloud()
