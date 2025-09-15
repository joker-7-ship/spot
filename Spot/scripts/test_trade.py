import requests
import pet_time_range(offset_start, offset_end):
    server_time = get_server_time()
    return server_time + offset_start, server_time + offset_end
starytest
import json
import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '../common')))
from common.request_utils import post_request, get_request, get_server_time
from data.trade_data import ACCESS,default,put_market,put_limit,order_cancel,order_pending,cancel_allorder,order_stop_limit,order_stop_market
from common.request_utils import post_request, get_request, get_server_time

@pytest.fixture
def server_time():
    return get_server_time()

def gt_time, end_time = get_time_range(-1000000, 3000000)

class TestBtcc:
# 下限价单
#     @pytest.mark.parametrize("data",put_limit)
    def test_put_limit(self, server_time):
        params = {
                "access_id": "aaf75ccf-4014-4fc7-b2c1-21cf3a8d6728",
                "tm": server_time,
                "market": "BTCUSDT",
                "side": 1,
                "option": 0,
                "amount": "1000",
                "price": "20000",
                "source": "U买B"
            }
        print("Params:", params)
        response = post_request("/btcc_api_trade/order/limit", params)
        print("Response:", response)
        global cancel_orderid
        cancel_orderid = response['result']['id']
        assert response['result']['id'] is not None, "Error"
# 下市价单
#     @pytest.mark.parametrize("data", put_market)
    def test_put_market(self,server_time):
        # params = {
        #     "access_id": data["access_id"],
        #     "tm": server_time,
        #     "market": data["market"],
        #     "side": data["side"],
        #     "option": data["option"],
        #     "amount": data["amount"],
        #     "source": data["source"]
        # }
        params ={
            "access_id": "aaf75ccf-4014-4fc7-b2c1-21cf3a8d6728",
            "tm": server_time,
            "market": "BTCUSDT",
            "side": 1,
            "amount": "1000",
            "option": 0,
            "source": "U买B"
        }
        print("Params:", params)
        response = post_request("btcc_api_trade/order/market", params)
        print("Response:", response)
        assert response['result']['id'] is not None, "Error"
# # 撤单
#     @pytest.mark.parametrize("data", order_cancel)
#     def test_order_cancel(self, server_time, data):
#         params = {
#             "access_id": data["access_id"],
#             "tm": server_time,
#             "market": data["market"],
#             "id":cancel_orderid
#         }
#         print("Params:", params)
#         response = post_request("/order/cancel", params)
#         print("Response:", response)
# # 查询用户挂单列表
#     ids_string = ""
#     @pytest.mark.parametrize("data", order_pending)
#     def test_order_pending(self, server_time, data):
#         global ids_string
#         params = {
#             "access_id": data["access_id"],
#             "tm": server_time,
#             "market": data["market"],
#             "side": data["side"],
#             "offset": data["offset"],
#             "limit": data["limit"]
#         }
#         print("Params:", params)
#         response = get_request("/order/pending", params)
#         print("Response:", response)
#         ids = [record['id'] for record in response['result']['records']]
#         TestBtcc.ids_string = '|'.join(map(str, ids))
# # 批量撤单
#     @pytest.mark.parametrize("data", default)
#     def test_order_cancelmulti(self, server_time, data):
#         params = {
#             "access_id": data["access_id"],
#             "tm": server_time,
#             "market": data["market"],
#             "order_ids":TestBtcc.ids_string
#         }
#         print("Params:", params)
#         response = post_request("/order/cancel_multi", params)
#         print("Response:", response)
# # 取消所有订单
#     @pytest.mark.parametrize("data", cancel_allorder)
#     def test_cancel_allorder(self, server_time, data):
#         params = {
#             "access_id": data["access_id"],
#             "tm": server_time,
#             "market": data["market"],
#             "side": data["side"]
#         }
#         print("Params:", params)
#         response = post_request("/order/cancel_all", params)
#         print("Response:", response)
#         assert response['error'] is None, "Error should be None"
# # 查询用户成交明细
#     @pytest.mark.parametrize("data", default)
#     def test_deal_history(self, server_time, data):
#         params = {
#             "access_id": data["access_id"],
#             "tm": server_time,
#             "market": data["market"],
#             "start_time": start_time,
#             "end_time": end_time,
#             "side": data["side"],
#             "offset": data["offset"],
#             "limit": data["limit"]
#         }
#         print("Params:", params)
#         response = get_request("/order/deal_history", params)
#         print("Response:", response)
#         global deals_orderid
#         deals_orderid = response['result']['records'][0]['order_id']
#         assert response['error'] is None, "Error should be None"
# # 查询用户订单成交明细
#     @pytest.mark.parametrize("data", default)
#     def test_order_deals(self, server_time, data):
#         params = {
#             "access_id": data["access_id"],
#             "tm": server_time,
#             "order_id": deals_orderid,
#             "side": data["side"],
#             "offset":data["offset"],
#             "limit":data["limit"]
#         }
#         print("Params:", params)
#         response = get_request("/order/deals", params)
#         print("Response:", response)
#         assert response['error'] is None, "Error should be None"
# # 查询用户订单历史记录
#     @pytest.mark.parametrize("data", default)
#     def test_order_finished(self, server_time, data):
#         params = {
#             "access_id": data["access_id"],
#             "tm": server_time,
#             "market": data["market"],
#             "start_time": start_time,
#             "end_time": end_time,
#             "side": data["side"],
#             "offset": data["offset"],
#             "limit": data["limit"]
#         }
#         print("Params:", params)
#         response = get_request("/order/finished", params)
#         print("Response:", response)
#         global finished_orderid
#         finished_orderid = response['result']['records'][0]['id']
#         assert response['error'] is None, "Error should be None"
# # 查询用户指定订单历史明细
#     def test_order_finisheddetail(self, server_time):
#         params = {
#             "access_id": ACCESS,
#             "tm": server_time,
#             "order_id":finished_orderid
#         }
#         print("Params:", params)
#         response = get_request("/order/finish_detail", params)
#         print("Response:", response)
# # 计划委托限价单
#     @pytest.mark.parametrize("data", order_stop_limit)
#     def test_order_stop_limit(self, server_time, data):
#         params = {
#             "access_id": data["access_id"],
#             "tm": server_time,
#             "market": data["market"],
#             "side": data["side"],
#             "stop_price": data["stop_price"],
#             "amount": data["amount"],
#             "price":data["price"],
#             "source": data["source"]
#         }
#         print("Params:", params)
#         response = post_request("/order/stop_limit", params)
#         print("Response:", response)
# # 计划委托市价单
#     @pytest.mark.parametrize("data", order_stop_market)
#     def test_order_stop_market(self, server_time, data):
#         params = {
#             "access_id": data["access_id"],
#             "tm": server_time,
#             "market": data["market"],
#             "side": data["side"],
#             "stop_price": data["stop_price"],
#             "amount": data["amount"],
#             "source": data["source"]
#         }
#         print("Params:", params)
#         response = post_request("/order/stop_market", params)
#         print("Response:", response)
# # 查询计划委托挂单列表
#     @pytest.mark.parametrize("data", default)
#     def test_order_pending_stop(self, server_time, data):
#         params = {
#             "access_id": data["access_id"],
#             "tm": server_time,
#             "market": data["market"],
#             "side": data["side"],
#             "offset": data["offset"],
#             "limit": data["limit"]
#         }
#         print("Params:", params)
#         response = get_request("/order/pending_stop", params)
#         print("Response:", response)
#         global cancle_stop_orderid
#         cancle_stop_orderid = response['result']['records'][0]['id']
# # 取消计划委托单
#     @pytest.mark.parametrize("data", default)
#     def test_order_cancle_stop(self, server_time, data):
#         params = {
#             "access_id": data["access_id"],
#             "tm": server_time,
#             "market": data["market"],
#             "order_id": cancle_stop_orderid
#         }
#         print("Params:", params)
#         response = post_request("/order/cancle_stop", params)
#         print("Response:", response)
# # 取消所有计划订单
#     @pytest.mark.parametrize("data", default)
#     def test_order_cancle_stop_all(self, server_time, data):
#         params = {
#             "access_id": data["access_id"],
#             "tm": server_time,
#             "market": data["market"],
#             "side": data["side"],
#         }
#         print("Params:", params)
#         response = post_request("/order/cancle_stop_all", params)
#         print("Response:", response)
# # 查询计划委托历史成交记录
#     @pytest.mark.parametrize("data", default)
#     def test_order_finished_stop(self, server_time, data):
#         params = {
#             "access_id": data["access_id"],
#             "tm": server_time,
#             "market": data["market"],
#             "start_time": start_time,
#             "end_time": end_time,
#             "side": data["side"],
#             "offset": data["offset"],
#             "limit": data["limit"]
#         }
#         print("Params:", params)
#         response = get_request("/order/finished_stop", params)
#         print("Response:", response)

# pytest.main(['--report=_report.html',
#              '--title=BtccSpotApiTest',
#              '--desc=基于Pytest的API自动化脚本',
#              '--template=2'])
# if __name__ == "__main":
#     TestBtcc()