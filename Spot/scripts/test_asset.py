import requests
import pytest
import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '../common')))
from common.request_utils import post_request, get_request, get_server_time
from data.asset_data import get_pending,asset_history,market_detail,market_kline,market_depth,asset_query
@pytest.fixture
def server_time():
    return get_server_time()
def get_time_range(offset_start, offset_end):
    server_time = get_server_time()
    return server_time + offset_start, server_time + offset_end
start_time, end_time = get_time_range(-1000000, 3000000)

class TestBtcc:
    @classmethod
# # 查询用户资产
#     @pytest.mark.parametrize("data", asset_query)
#     def test_asset_query(self, server_time, data):
#         params = {
#             "access_id": data["access_id"],
#             "tm": server_time,
#         }
#         print("params:", params)
#         response = get_request("/asset/query", params)
#         print("Response:", response)
#         assert response['error'] is None, "Error should be None"
# # 查询用户资金流水
#     @pytest.mark.parametrize("data", asset_history)
#     def test_asset_history(self, server_time, data):
#         params = {
#             "access_id": data["access_id"],
#             "tm": server_time,
#             "asset": data["asset"],
#             "business": data["business"],
#             "start_time": start_time,
#             "end_time": server_time,
#             "offset": data["offset"],
#             "limit": data["limit"]
#         }
#         print("Params:", params)
#         response = get_request("/asset/query_history", params)
#         print("Response:", response)
# # 查询所有交易对信息
#     def test_market_list(self):
#         response = get_request("/market/list", params={})
#         print("Response:", response)
# # 查询单个交易对信息
#     @pytest.mark.parametrize("data", market_detail)
#     def test_market_detail(self,data):
#         params={"market":data["market"]}
#         response = get_request("/market/detail", params)
#         print("Response:", response)
#         assert response['result'].get('name') is not None, "name should not be None"

# 查询单个交易对信息
    def test_market_detail(self):
        params = {"market":"FDDUSDT"}
        response = get_request("/market/detail", params)
        print("Response:", response)
        assert response['result'].get('name') is not None, "name should not be None"

# 查询k线
    @pytest.mark.parametrize("data", market_kline)
    def test_market_kline(self,data):
        params={
            "market":data["market"],
            "start_time": start_time,
            "end_time": end_time,
            "interval": data["interval"],
        }
        print("Params:", params)
        response = get_request("/market/kline", params)
        print("Response:", response)
        assert response['error'] is None, "Error should be None"
# # 查询深度
#     @pytest.mark.parametrize("data", market_depth)
#     def test_market_depth(self,data):
#         params={
#             "market":data["market"],
#             "limit": data["limit"],
#             "merge": data["merge"],
#         }
#         print("Params:", params)
#         response = get_request("/market/depth", params)
#         print("Response:", response)
#         assert response['result'].get('time') is not None, "Time should not be None"

    # 查询深度
    def test_market_depth(self,):
        params = {
            "market": "1000CAWUSDT",
            "limit": "50",
            "merge": "0.00000001"
        }
        print("Params:", params)
        response = get_request("/market/depth", params)
        print("Response:", response)
        assert response['result'].get('time') is not None, "Time should not be None"

# 查询最新价
    @pytest.mark.parametrize("data", market_detail)
    def test_market_last(self,data):
        params={"market":data["market"]}
        print("Params:", params)
        response = get_request("/market/last", params)
        print("Response:", response)
        assert response['error'] is None, "Error should be None"
# pytest.main(['--report=_report.html',
#              '--title=BtccSpotApiTest',
#              '--desc=基于Pytest的API自动化脚本',
#              '--template=2'])
# if __name__ == "__main":
#     TestBtcc()