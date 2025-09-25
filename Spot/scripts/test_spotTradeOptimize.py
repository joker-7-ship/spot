import requests
import pytest
import json
import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '../common')))
from common.request_utils import post_request, get_request, get_server_time
from data.trade_data import ACCESS, default, put_market,put_limit,order_cancel,order_pending,cancel_allorder,order_stop_limit,order_stop_market
from common.request_utils import post_request, get_request, get_server_time

@pytest.fixture
def server_time():
    return get_server_time()

def get_time_range(offset_start, offset_end):
    server_time = get_server_time()
    return server_time + offset_start, server_time + offset_end

start_time,  end_time = get_time_range(-1000000, 3000000)

class TestBtcc:

    # # 整合下单接口：POST /trade/v2/order （對標Binance: 整合limit, market, plan limit, plan market）

    # def test_Limit_place_order(self, server_time):
    #     params = {
    #          "access_id": "8f8b43f3-d8c3-4210-98dc-11bb464dcc68",
    #          "tm": server_time,
    #          "type": "LIMIT",
    #          "market": "BTCUSDT",
    #          "side": "SELL",
    #          "amount": "0.02",
    #          "price": "114000",
    #          "source": "android"
    #      }
    #
    #     response = post_request("/order/place_order", params)
    #     print(response)
    #     assert response['result'] is not None, "Error"
# 市价单 amount单位是usdt
#     def test_Market_place_order(self, server_time):
#         params = {
#              "access_id": "8f8b43f3-d8c3-4210-98dc-11bb464dcc68",
#              "tm": server_time,
#              "type": "MARKET",
#              "market": "BTCUSDT",
#              "side": "SELL",
#              "amount": "0.02",
#              "time_in_force": 0,
#              "source": "android"
#          }
#         response = post_request("/order/place_order", params)
#         print(response)
#         assert response['result'] is not None, "Error"

    # def test_Stop_Limit_place_order(self, server_time):
    #     params = {
    #         "access_id": "8f8b43f3-d8c3-4210-98dc-11bb464dcc68",
    #         "tm": server_time,
    #         "type": "STOP_LIMIT",
    #         "market": "BTCUSDT",
    #         "side": "SELL",
    #         "amount": "0.02",
    #         "price": "114277",
    #         "stop_price": "114333",
    #         "source": "android"
    #     }
    #     response = post_request("/order/place_order", params)
    #     print(response)
    #     assert response['result'] is not None, "Error"

    # def test_Stop_Market_place_order(self, server_time):
    #     params = {
    #         "access_id": "8f8b43f3-d8c3-4210-98dc-11bb464dcc68",
    #         "tm": server_time,
    #         "type": "STOP_MARKET",
    #         "market": "BTCUSDT",
    #         "side": "SELL",
    #         "amount": "0.02",
    #         "stop_price": "114333",
    #         "source": "android"
    #
    #     }
    #     response = post_request("/order/place_order", params)
    #     print(response)
    #     assert response['result'] is not None, "Error"





    # 新增改单接口：POST /trade/order/amend-order (對標OKX: 新增改單功能; 可改價格和數量但是會影響搓合優先順序)
    def test_Amend_order(self, server_time):
        params = {
                "access_id": "8f8b43f3-d8c3-4210-98dc-11bb464dcc68",
                "tm": server_time,
                "market": "BTCUSDT",
                "order_id":1088522458,
                "new_amount": "2.1",
                "new_price": "112322",
            }
        response = post_request("/order/amend_order_data", params)
        print(response)
        assert response['result'] is not None, "Error"


    # # 新增改单接口：POST /trade/order/amend-keepPriority (對標Binance: 新增改量功能; 只能往下改數量; 不影響搓合順序)

    def test_Amend_Keep_Priority(self, server_time):
        params = {
                "access_id": "8f8b43f3-d8c3-4210-98dc-11bb464dcc68",
                "tm": server_time,
                "market": "BTCUSDT",
                "order_id": 1088522458,
                "new_amount": "1"
            }
        response = post_request("/order/amend_order_amount", params)
        print(response)
        assert response['result'] is not None, "Error"








# 查询用户挂单列表
    ids_string = ""
    @pytest.mark.parametrize("data", order_pending)
    def test_order_pending(self, server_time, data):
        global ids_string
        params = {
            "access_id": data["access_id"],
            "tm": server_time,
            "market": data["market"],
            "side": data["side"],
            "offset": data["offset"],
            "limit": data["limit"]
        }
        print("Params:", params)
        response = get_request("/order/pending", params)
        print("Response:", response)
        ids = [record['id'] for record in response['result']['records']]
        TestBtcc.ids_string = '|'.join(map(str, ids))
#
#     # 查询深度优化，增加请求深度
#     def test_MarketDepth(self, server_time):
#         params = {
#                 "tm": server_time,
#                 "market": "BTCUSDT",
#                 "limit": 50,
#                 "merge": 0.1
#             }
#         response = get_request("/market/depth", params)
#         print(response)
#         assert response['result'] is not None, "Error"

