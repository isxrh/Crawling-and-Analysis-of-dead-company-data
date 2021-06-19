## 死亡公司数据爬取与分析

> 📝Python大作业
> 

### 01. 目录及文件说明

- `dates`：存放爬取数据目录
- `html`：存数据分析图目录
- `images`：存放UI界面图标目录
- `deadNum_year.py`：爬取2014-2020年每年死亡公司数目代码
- `getdates.py`：用于爬取数据代码（从网页第一页开始爬取）
- `getdate2018.py`：用于爬取2018年数据代码（与getdates.py稍有不同：从指定页数爬取）
- `cityMap.py`：生成死亡公司城市分布地图代码
- `companyType`：生成死亡公司类型词云图代码
- `liveTimeAnalyze.py`：生成死亡时间分布柱状图代码
- `statusAnalyze.py`：生成死亡公司融资状态分布饼图的代码
- `UI.py`：数据分析展示主界面代码
- `ui2017.py`：2017年数据分析展示界面代码
- `ui2018.py`：2018年数据分析展示界面代码
- `ui2019.py`：2019年数据分析展示界面代码
- `ui2020.py`：2020年数据分析展示界面代码
- `findCompany.py`：查询产业对应的公司代码

### 02. env
`python 3.8`
`pyecharts` `csv` `selenium` `time` `re` `pandas` `PyQt5` `qdarkstyle` `sys` `functools` `collections`

### 03. 界面展示
- #### 主界面
![img.png](./images/主界面效果展示.png)
- #### 二级界面
（仅展示2020年）
![img_1.png](./images/二级界面效果展示.png)







