# -*- coding: utf-8 -*-
# Time : 2023/5/12 21:29
# Author : xx
# File : conftest.py
# Desc :

import pytest
from selenium import webdriver
from selenium.webdriver.edge.service import Service


@pytest.fixture(scope="session")
def login():
    e=Service(executable_path=r'D:\driver\msedgedriver.exe')
    driver=webdriver.Edge(service=e)
    driver.maximize_window()
    driver.get('http://127.0.0.1/zentao/user-login-L3plbnRhby8=.html')
    yield driver
    driver.quit()






