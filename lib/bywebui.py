from hytest import *
from selenium import webdriver


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
