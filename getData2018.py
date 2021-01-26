# -*- coding:utf-8 -*-
# 爬取IT桔子网死亡公司库数据
# URL:https://www.itjuzi.com/deathCompany

from selenium import webdriver
from selenium.webdriver.support.wait import WebDriverWait
import time

browser = webdriver.Chrome()
browser.maximize_window()  # 最大化窗口
wait = WebDriverWait(browser, 10)  # 等待加载10s

def login():
    '''
    功能：模拟登录
    登录账号：15168178971
    账号密码：123456
    '''
    browser.get('https://www.itjuzi.com/user/login')
    browser.find_element_by_xpath('//*[@id="app"]/div[1]/div[2]/div/div/div/div/div[2]/div[1]/form/div[1]/div/div['
                                  '1]/input').send_keys('15168178971')   # 输入账号
    browser.find_element_by_xpath('//*[@id="app"]/div[1]/div[2]/div/div/div/div/div[2]/div[1]/form/div[2]/div/div['
                                  '1]/input').send_keys('123456')  # 输入密码
    browser.find_element_by_xpath('//*[@id="app"]/div[1]/div[2]/div/div/div/div/div[2]/div[1]/div/button').click()
    time.sleep(5)
    get_deathCompany_page()


def get_deathCompany_page():
    '''
    功能：爬取死亡公司信息，并写入deathCompany.csv文件
    '''
    browser.get('https://www.itjuzi.com/deathCompany')
    time.sleep(3)

    # 起始爬取页数
    page_textbox = browser.find_element_by_xpath('//*[@id="app"]/div[1]/div/div/div/div[2]/div/div[3]/div[2]/div/div/span/div/input');
    page_textbox.clear();
    page_textbox.send_keys(683);     # 从第683页开始爬取

    for page in range(1, 100):   # 爬取70页
        result = []     # 存放每页的爬取数据

        dead_company = browser.find_element_by_tag_name("table").find_elements_by_tag_name('tr')
        length = len(dead_company)      # 每页公司数目
        for i in range(1, length):
            # 依次爬取同一页的每一条公司数据
            dc = dead_company[i - 1]
            # 公司名称
            company_name = dc.find_element_by_xpath('//*[@id="app"]/div[1]/div/div/div/div[2]/div/div[3]/div['
                                                    '2]/table/tbody/tr['+str(i)+']/td[3]/div/h5/a').text  # 公司名称
            # 存活时间
            live_time = dc.find_element_by_xpath('//*[@id="app"]/div[1]/div/div/div/div[2]/div/div[3]/div['
                                                 '2]/table/tbody/tr['+str(i)+']/td[3]/div/p').text  # 存活时间
            # 成立时间
            setup_time = dc.find_element_by_xpath('//*[@id="app"]/div[1]/div/div/div/div[2]/div/div[3]/div['
                                                  '2]/table/tbody/tr['+str(i)+']/td[7]').text  # 成立时间
            # 关闭时间
            close_time = dc.find_element_by_xpath('//*[@id="app"]/div[1]/div/div/div/div[2]/div/div[3]/div['
                                                  '2]/table/tbody/tr['+str(i)+']/td[4]').text  # 关闭时间
            # 所属行业
            company_category = dc.find_element_by_xpath('//*[@id="app"]/div[1]/div/div/div/div[2]/div/div[3]/div['
                                                        '2]/table/tbody/tr['+str(i)+']/td[5]').text  # 所属行业
            # 公司地点
            company_province = dc.find_element_by_xpath('//*[@id="app"]/div[1]/div/div/div/div[2]/div/div[3]/div['
                                                        '2]/table/tbody/tr['+str(i)+']/td[6]').text  # 公司地点
            # 投获状态
            received_status = dc.find_element_by_xpath('//*[@id="app"]/div[1]/div/div/div/div[2]/div/div[3]/div['
                                                       '2]/table/tbody/tr['+str(i)+']/td[8]').text  # 投获状态
            # 数据存入result列表
            result.append(','.join(
                [company_name, live_time, setup_time, close_time, company_category, company_province, received_status]))

        with open('683_.csv', 'a') as f:
            # 存入文件
            f.write('\n'.join('{}'.format(id) for id in result) + '\n')
            print(result)

        print('已爬取第{}页。'.format(page))

        browser.find_element_by_class_name('btn-next').click()  # 点击下一页
        time.sleep(3)


if __name__ == "__main__":
    login()
