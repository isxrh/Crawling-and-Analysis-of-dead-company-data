# 2014-2020年倒闭公司数目折线图
from pyecharts.charts import Line

def deadNum():
    attr = ["2014", "2015", "2016", "2017", "2018", "2019", "2020"]
    count = [347, 1032, 1639, 2482, 2478, 5047, 973]

    line=(
        Line()
        .add_xaxis(attr)
        .add_yaxis("倒闭公司数目", count)
        # .set_global_opts(title_opts=opts.TitleOpts(title='2014-2020年倒闭公司数目'))
    )
    line.render('./html/numLineChart.html')


if __name__ == "__main__":
    deadNum()