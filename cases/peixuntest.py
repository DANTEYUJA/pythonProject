# 对应lib套件下的cmtclogin文件中 声明的cmtc_login方法
from time import sleep

from hytest import *
from hytest import STEP, INFO
from selenium.webdriver.common.by import By

# from selenium.webdriver.support.ui import Select
from lib.cmtclg_hsh import cmtc_login


class cmtc002:
    name = '培训审核流程 cmtc002'
    tags = ['1235']

    # 初始化方法setup  登录
    # 对象wd调用lib/cmtclogin中cmtc_login
    def setup(self):
        INFO('初始化登录流程')
        cmtc_login()
        STEP(1, '登录成功')

    # 测试用例开始执行
    def teststeps(self):
        # 从lib cmtclogin中取出gstore方法中的wd对象
        wd = GSTORE['wd']
        # 隐式等待
        wd.implicitly_wait(10)
        STEP(2, '新增培训申请-花松鹤')
        wd.find_element(By.CSS_SELECTOR, "div:nth-child(7) > .el-menu-item").click()
        wd.find_element(By.CSS_SELECTOR, "div:nth-child(2) > a span").click()
        # 新建培训申请弹框
        wd.find_element(By.CSS_SELECTOR, ".el-col > .el-button--primary").click()
        wd.find_element(By.CSS_SELECTOR,
                        "div#training-info div:nth-child(1) > div > div > div > div > div > span > span > i").click()
        sleep(1)
        # 计划内培训下拉框


    def teardown(self):
        wd = GSTORE['wd']
        wd.find_element_by_xpath("/html/body/div/div/form/div[1]/div/div[1]/input").clear()
        wd.find_element_by_xpath("/html/body/div/div/form/div[2]/div/div/input").clear()
