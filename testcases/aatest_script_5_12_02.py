# -*- coding: utf-8 -*-
# Time : 2023/5/12 20:03
# Author : xx
# File : test_script_5_12_0002.py
# Desc :mark的自定义，跳过，传参，排序,引用,重跑失败用例

import pytest
import allure

# @pytest.mark.usefixtures('login1')    #引用(conftest.py中的login1)
@allure.feature('登录模块')
class TestCases2:
    # @pytest.mark.flaky(reruns=3)
    # @pytest.mark.run(order=2)

    # @pytest.mark.xxx         #pytest.mark.自定义名称

    # @pytest.mark.skip()
    # @pytest.mark.skipif(2<3,reason='跳过')
    @allure.story('登录成功的测试用例')
    def test_3(self):
        with allure.step('输入用户名和密码'):
            print('用户名和密码')
        with allure.step('点击登录'):
            print('点击登录按钮')

        # assert 2>3

    @allure.story('登录失败的测试用例')
    def test_4(self):
        print('第四个测试用例')
    # @pytest.mark.run(order=1)

    # @pytest.mark.parametrize('username,password',[('test001','12345'),('test002','123456')])
    # def test_4(self,username,password):
    #     print(f'第四个测试用例{username},{password}')



if __name__=='__main__':
    # pytest.main(['-s','-v','--setup-show','-m xxx'])    #执行做标记(xxx)的
    pytest.main(['-s', '-v'])