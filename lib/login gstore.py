from lib.webui import *


# 我们在创建 WebDriver 对象后，把它存到了 hytest 全局存储对象 GSTORE 中。 方便其他的代码 获取。
class UI_0102:

    # 测试用例步骤
    def teststeps(self):
        STEP(1, '登录网站')
        open_browser()
        mgr_login()

        # 下面是其余代码


def open_browser():
    INFO('打开浏览器')
    options = webdriver.ChromeOptions()
    options.add_experimental_option('excludeSwitches', ['enable-logging'])

    wd = webdriver.Chrome(options=options)
    wd.implicitly_wait(10)

    GSTORE['wd'] = wd


def mgr_login():
    wd = GSTORE['wd']

    wd.get('http://127.0.0.1/mgr/sign.html')

    wd.find_element_by_id('username').send_keys('byhy')
    wd.find_element_by_id('password').send_keys('88888888')

    wd.find_element_by_tag_name('button').click()
