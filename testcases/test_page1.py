# -*- coding: utf-8 -*-
# Time : 2023/5/6 20:35
# Author : xx
# File : test_page1.py
# Desc :


from time import sleep
from objectpage.login_page import LoginPage
from config.config import system_version
from data.data import ReadWrite
from log.log import logger
import allure

# import pytest
# user_list=ReadWrite().excelread('users')
@allure.feature('登录模块')
class TestCases:
    # @pytest.mark.parametrize('username,password',user_list)
    @allure.story('登录和退出测试用例')
    def test_1(self,login):
        '''
        验证有效的用户名和密码成功登录系统
        '''
        print('登录的第一个测试用例')

        self.driver=login
        self.loginpage=LoginPage(self.driver)
        user_list=ReadWrite().excelread('users')
        username=user_list[0][0]
        password=user_list[0][1]
        with allure.step('输入用户名和密码'):
            self.loginpage.input_username(username)
            self.loginpage.input_password(password)
        with allure.step('点击登录'):
            self.loginpage.click_login()
        sleep(1)

        assert('地盘 - 禅道' in self.driver.title)    #断言
        with allure.step('点击退出'):
            self.loginpage.click_logout()   #不执行此处时，可封装到teardown中
        logger.info('有效的用户名和密码成功登录系统')

    # # @unittest.skip       #'不执行该测试用例'
    # @unittest.skipIf(system_version=='1.1',reason='只有版本号为1.2才执行')
    # def test_2(self):
    #     '''
    #     验证密码为空登录失败
    #     '''
    #     print('登录第二个测试用例')
    #     # sleep(1)
    #     # self.driver.find_element(By.ID, 'account').send_keys('admin')
    #     # self.driver.find_element(By.ID, 'submit').click()
    #     # sleep(1)
    #     # alert_login=self.driver.switch_to.alert
    #     # alert_login.accept()
    #
    #     self.loginpage.input_username('admin')
    #     self.loginpage.click_login()
    #     sleep(1)
    #     alert_login=self.driver.switch_to.alert
    #     alert_login.accept()