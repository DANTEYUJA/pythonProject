from time import sleep

from hytest import *
from hytest import INFO
from selenium import webdriver


# 我们在创建 WebDriver 对象后，把它存到了 hytest 全局存储对象 GSTORE 中。 方便其他的代码 获取。
# 公共代码‘登录’放入lib库中
# 声明open_browser对象 打开浏览器
def open_browser():
    INFO('打开浏览器至消防页面')
    # 创建浏览器对象wd/调用驱动打开chrome
    wd = webdriver.Chrome(r'c:\webdrivers\chromedriver.exe')
    #浏览器最大化
    wd.get_window_size()
    wd.maximize_window()
#以下代码表示将上方登录代码存入GSTORE对象中方便调用 存入是GSTORE在前
    GSTORE['wd'] = wd

# 因为firewebopen调用全局对象GSTORE
def mgr_login():
    # 调用是wd对象在前
    wd = GSTORE['wd']
    # wd.get('http://firecontrol.console.rayjeak.com/sign/login')
    wd.find_element_by_id('userName').send_keys('admin')
    wd.find_element_by_id('password').send_keys('888888')
    wd.find_element_by_xpath('//*[@id="root"]/section/main/section/main/form/div[4]/div/div/span/button').click()
    sleep(2)
