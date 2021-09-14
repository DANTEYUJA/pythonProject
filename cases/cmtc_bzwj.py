# 对应lib套件下的cmtclogin文件中 声明的cmtc_login方法
from time import sleep

from hytest import *
from hytest import STEP, INFO
from selenium.common.exceptions import *
from selenium.webdriver.support.wait import WebDriverWait

from lib.cmtclg_hsh import cmtc_login


# from selenium.webdriver.support.ui import Select

class cmtc001:
    name = '新建标准文件'
    tags = ['1234']

    # 初始化方法setup  登录
    # wd调用lib/cmtclogin中cmtc_login
    def setup(self):
        INFO('初始化登录流程')
        cmtc_login()
        STEP(1, '登录')

    # 清除方法
    def teardown(self):
        wd = GSTORE['wd']
        wd.quit()

    # 测试用例开始执行
    def teststeps(self):
        # 从lib cmtclogin中取出gstore方法中的wd变量
        wd = GSTORE['wd']
        # 隐式等待
        wd.implicitly_wait(10)
        STEP(2, '文件管理菜单检查')
        # 文件管理 div#app div:nth-child(9) > li'表示ul标签下第9个div下的li元素
        wd.find_element_by_css_selector(
            'div#app div:nth-child(9) > li').click()
        # 定义变量菜单menu获取内容 并用check_point检查菜单是否符合 注：一定要定位到文案标签头span 缩小定位范围很重要
        wd.find_elements_by_css_selector(
            '#app > div > div.main-container.hasTagsView > div > div > div.scrollbar-wrapper.el-scrollbar__wrap')
        wd.implicitly_wait(10)
        eles = wd.find_elements_by_css_selector(
            '#app > div > div.main-container.hasTagsView > div > div > div.scrollbar-wrapper.el-scrollbar__wrap > div > ul > div > a > li > span')
        menuText = [ele.text for ele in eles]
        INFO(menuText)
        # 总共四个模块，所以是[:4]
        CHECK_POINT('左侧菜单检查', menuText[:4] == ['标准文件', '标准文件目录管理', '程序文件', '程序文件目录管理'], True)
        print(menuText)
        WebDriverWait(wd, 10)

        STEP(3, '标准文件查询')
        wd.find_element_by_css_selector('#app > div > div.main-container.hasTagsView > div > div > div.scrollbar-wrapper.el-scrollbar__wrap > div > ul > div:nth-child(1) > a > li > span').click()
        # 搜索内容标准文件dd \换行
        wd.find_element_by_css_selector('div#app div.el-input.el-input--medium.el-input--prefix > input').send_keys(
            'dd')
        # 搜索
        wd.find_element_by_css_selector(
            '#app > div > div.main-container.hasTagsView > section > div.maintenanceBox > div.maintenance-content.el-row > div.el-col.el-col-20 > div:nth-child(1) > button').click()
        sleep(1)
        def isElementPresent(by, value):
            try:
                dd = wd.find_element(by=by, value=value)
            except NoSuchElementException as dd:
                # 打印异常信息
                print(dd)
                # 发生了NoSuchElementException异常，说明页面中未找到该元素，返回False
                return False
            else:
                # 没有发生异常，表示在页面中找到了该元素，返回True
                return True

        def test_isElementPresent():
            # 判断页面元素id属性值为“query”的页面元素是否存在
            res = wd.isElementPresent("class", "standardNoSpan")
            if res is True:
                print("所查找的元素存在于页面上！")
            else:
                print("页面中未找到所需要的页面元素！")

        # 向下滚动500个像素
        wd.execute_script('window.scrollBy(0,1000)')

        sleep(2)
        STEP(4, '新增标准文件')
        # 新建标准文件
        wd.implicitly_wait(10)
        wd.find_element_by_css_selector(
            'div#app div.maintenance-export > button[type="button"]:nth-child(1) > span').click()
        wd.implicitly_wait(10)
        wd.find_element_by_css_selector(
            'div#app form > div:nth-child(1) > div:nth-child(1) > div > div > div > input').send_keys('ddauto1')
        wd.find_element_by_css_selector(
            '#app > div > div.main-container.hasTagsView > section > div.maintenanceBox > div.el-dialog__wrapper.dialogAdd > div > div.el-dialog__body > div > div:nth-child(2) > form > div:nth-child(1) > div:nth-child(2) > div > div > div.el-input.el-input--medium > input').send_keys(
            '滴滴测试1')
        # 英文名称
        wd.find_element_by_css_selector(
            'div#app div:nth-child(1) > div:nth-child(3) > div > div > div > input').send_keys('ddenglish')
        # 中标分类
        wd.find_element_by_css_selector(
            'div#app form > div:nth-child(2) > div:nth-child(1) > div > div > div > input').send_keys('dd中标分类1')
        # ICS分类
        wd.find_element_by_css_selector(
            'div#app form > div:nth-child(2) > div:nth-child(2) > div > div > div > input').send_keys('ddISC分类1')
        # 标准分类编号
        wd.find_element_by_css_selector(
            'div#app div:nth-child(2) > div:nth-child(3) > div > div > div > input').send_keys('dd13123124124312')
        # 标引依据
        wd.find_element_by_css_selector(
            'div#app div.el-col.el-col-16 > div > div > div > input').send_keys('dd依据1')
        wd.find_element_by_css_selector(
            'div#app form > div:nth-child(2) > div:nth-child(2) > div > div > div > input').send_keys('ddISC分类1')
        # 复审结果
        wd.find_element_by_css_selector(
            'div#app div:nth-child(3) > div.el-col.el-col-8 > div > div > div > input').send_keys('dd复审结果通过')
        # 所属目录
        wd.find_element_by_css_selector(
            'div#app div:nth-child(4) > div:nth-child(1) > div > div > div > div > button[type="button"] > span').click()
        wd.implicitly_wait(10)
        # 选择标准目录GB
        wd.find_element_by_css_selector(
            '#app > div > div.main-container.hasTagsView > section > div.maintenanceBox > div:nth-child(4) > div > div.el-dialog__body').click()
        wd.find_element_by_css_selector(
            'div#app div:nth-child(4) > div > div.el-dialog__footer > span > button[type="button"].el-button.el-button--primary.el-button--medium > span').click()

        # remark备注
        wd.find_element_by_css_selector(
            'div#app textarea').send_keys('dd自动化测试国标文件1')

        # 关联穿梭框流程
        csk = wd.find_element_by_css_selector(
            'div#app div:nth-child(7) > div > div > div > div > div:nth-child(1)')
        wd.implicitly_wait(10)
        csk.find_element_by_css_selector(
            '#app > div > div.main-container.hasTagsView > section > div.maintenanceBox > div.el-dialog__wrapper.dialogAdd > div > div.el-dialog__body > div > div:nth-child(2) > form > div:nth-child(7) > div > div > div > div > div:nth-child(1) > div > div.el-checkbox-group.el-transfer-panel__list.is-filterable > label:nth-child(3) > span.el-checkbox__label > span').click()
        wd.find_element_by_css_selector(
            'div#app span.el-checkbox__input.is-focus > span').click()
        WebDriverWait(wd, 10)
        # 文件上传
        # 使用os调用本地autoit.exe上传图片，注意autoit.exe需要在运行状态
        wd.find_element_by_css_selector(
            'div#app div:nth-child(6) > div:nth-child(1) > div > div > div > div > button[type="button"] > span').click()
        sleep(1)
        os.system(r'D:\autoit.exe')
        sleep(5)
        # 截屏 第1个参数是 webdriver 对象
        # width 参数为可选参数， 指定图片显示宽度
        SELENIUM_LOG_SCREEN(wd, width='50%')
        sleep(5)
        # 保存
        wd.find_element_by_css_selector(
            'div#app div.el-dialog__wrapper.dialogAdd > div > div.el-dialog__footer > span > button[type="button"].el-button.el-button--primary.el-button--medium > span').click()
