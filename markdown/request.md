~~~
# -*- coding: UTF-8 -*-
import json
import requests


def get_http_response(req_url, req_params):
    """HTTP请求.

    Args:
        req_url: 请求地址.
        req_params: 请求参数,dict类型.

    Returns:
        请求返回结果，json类型.
    """
    headers = {'Content-Type': "application/json"}
    response = requests.post(url=req_url, data=json.dumps(req_params), headers=headers)
    response_data = json.loads(response.text)
    return response_data
~~~