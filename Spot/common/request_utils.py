"""
============================
Project:BtccSpotApiTest
Address:https://www.cryptouat.com/
Author:Binea
Time:2024/09
============================
"""
import hashlib
import urllib.parse
import requests
import time
from common.config import ACCESS_ID, SECRET_KEY, BASE_URL

# # 获取服务器时间戳
# def get_server_time():
#     response = requests.get(f"{BASE_URL}/btcc_trade/time", verify=False)
#     if response.status_code == 200:
#         return response.json()["data"]
#     else:
#         raise Exception("无法获取服务器时间")

# 获取服务器时间戳
def get_server_time():
    response = requests.get("https://spot_api.btcccdn.com:9910/btcc_api_trade/time", verify=False)
    if response.status_code == 200:
        return response.json()["data"]
    else:
        raise Exception("无法获取服务器时间")

# 对参数进行排序并生成 MD5 签名
def generate_signature(params):
    param_str = '&'.join([f'{k}={v}' for k, v in params.items()])
    param_str_with_key = f'{param_str}&secret_key={SECRET_KEY}'
    sorted_param_str = '&'.join(sorted(param_str_with_key.split('&')))
    md5_signature = hashlib.md5(sorted_param_str.encode('utf-8')).hexdigest()
    print("Sign:", sorted_param_str)
    return md5_signature

# headers生成
def prepare_request(params):
    signature = generate_signature(params)
    return {'authorization': signature}

# 发送 POST 请求
def post_request(endpoint, params, verify=False):
    url = f"{BASE_URL}{endpoint}"
    headers = prepare_request(params)
    response = requests.post(url, headers=headers, json=params, verify=verify)
    response.raise_for_status()  # 抛出异常以处理 HTTP 错误
    return response.json()

# 发送 GET 请求
def get_request(endpoint, params=None, verify=False):
    params = params or {}
    url = f"{BASE_URL}{endpoint}?{urllib.parse.urlencode(params)}"
    headers = prepare_request(params)
    response = requests.get(url, headers=headers, verify=verify)
    response.raise_for_status()  # 抛出异常以处理 HTTP 错误
    return response.json()

if __name__ == "__main__":
    try:
        server_time = get_server_time()
        print("服务器时间:", server_time)
    except Exception as e:
        print("错误:", e)