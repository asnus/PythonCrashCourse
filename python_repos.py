# -*- coding: utf-8 -*-
"""
Created on Tue Dec 25 15:29:07 2018

@author: lzh
"""

import requests

#执行API调用并存储响应
url = 'https://api.github.com/search/repositories?q=language:python&sort=stars'
r = requests.get(url)
print(type(r))
print("Status code:",r.status_code)

#将api响应存储在一个变量中
response_dict = r.json()

#处理结果
print(response_dict.keys())