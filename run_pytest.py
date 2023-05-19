# -*- coding: utf-8 -*-
# Time : 2023/5/12 21:52
# Author : xx
# File : run_pytest.py
# Desc :

import pytest
import subprocess

pytest.main()
subprocess.call('allure generate ./result/temp -o ./result/report --clean',shell=True)  # subprocess调用  generate 生成 从./result/temp中转换为html放到./result/report
subprocess.call('allure open -h 127.0.0.1 -p 8883 ./result/report',shell=True) #生成一个本地的服务并自动打开html报告