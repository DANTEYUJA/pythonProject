# 对应lib套件下的webui文件中 声明的 open_browser, mgr_login 方法
from time import sleep

from hytest import *
from hytest import CHECK_POINT

from lib.webui import open_browser


# 导入Select类

class c0001:
       name = '登录测试 c0001'

       # 初始化方法setup  登录模块
       # 对象wd调用lib/webui中open_browser，mgr_login()
       def setup(self):
           open_browser()

       def teststeps(self):
           wd =GSTORE['wd']
           wd.find_element_by_id('userName').send_keys('adm')
           wd.find_element_by_id('password').send_keys('888')
           wd.find_element_by_xpath('//*[@id="root"]/section/main/section/main/form/div[4]/div/div/span/button').click()
           sleep(2)

           notify = wd.switch_to.alert.text
           print(notify)
           CHECK_POINT('弹出提示', notify == '出错了 用户名或者密码错误')

       # clear清空数据
       def teardown(self):
           wd =GSTORE['wd']
           wd.find_element_by_id('userName').clear()
           wd.find_element_by_id('password').clear()






