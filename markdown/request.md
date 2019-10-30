~~~
# -*- coding: UTF-8 -*-
import requests
import json


def get_response(req_url, req_params):
    """请求"""
    headers = {'Content-Type': "application/json"}
    req = requests.post(url=req_url, data=json.dumps(req_params), headers=headers)
    res_json = json.loads(req.text)
    return res_json
~~~