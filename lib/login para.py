from lib.webui import*


class UI_000x:
    ddt_cases = [
        {
            'name': '登录 UI_0001',
            'para': [None, '88888888', '请输入用户名']
        },
        {
            'name': '登录 UI_0002',
            'para': ['byhy', None, '请输入密码']
        },
        {
            'name': '登录 UI_0003',
            'para': ['byh', '88888888', '登录失败 : 用户名或者密码错误']
        }
    ]

    def teststeps(self):
        wd = GSTORE['wd']

        wd.get('http://127.0.0.1:8047/mgr/sign.html')

        username, password, info = self.para

        if username is not None:
            wd.find_element_by_id('username').send_keys(username)

        if password is not None:
            wd.find_element_by_id('password').send_keys(password)

        wd.find_element_by_tag_name('button').click()

        sleep(2)

        notify = wd.switch_to.alert.text

        CHECK_POINT('弹出提示', notify == info)

        wd.switch_to.alert.accept()

    def teardown(self):
        wd = GSTORE['wd']
        wd.find_element_by_id('username').clear()
        wd.find_element_by_id('password').clear()
