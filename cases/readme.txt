python项目必须包含cases套件，python包内容必须包含class用例类，参数化必须包含初始化setup与teardown方法，需要在
teststeps测试步骤前用来初始化’登录‘这个操作，class用例下必须包含teststeps测试方法
整体框架为：class>setup>teardown>teststeps>step>info>check_point

lib.webui.py=正常登录流程 全局变量
lib.webopen.py=打开浏览器到消防页面
cases/firecontrol/failcontrol.py 当前套件变量
lib.firecsh.py=异常用例登录校验用例
