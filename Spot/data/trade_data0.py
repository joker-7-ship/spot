from common.config import ACCESS_ID,offset,limit
ACCESS = "aaf75ccf-4014-4fc7-b2c1-21cf3a8d6728"
default = [
    {
        "access_id": ACCESS_ID,
        "market": "BTCUSDT",
        "side": 2,
        "option": 0,
        "amount": "1",
        "price": "20000.34",
        "stop_price": "60000.11",
        "source": "python example",
        "offset": offset,
        "limit": limit
    },
    {
        "access_id": ACCESS_ID,
        "market": "ETHUSDT",
        "side": 1,
        "option": 1,
        "amount": "0.5",
        "price": "3000.50",
        "stop_price": "4000.00",
        "source": "Valid source",
        "offset": offset,
        "limit": limit
    },
    # 缺少参数
    {
        "market": "BTCUSDT",  # 缺少 access_id
        "side": 2,
        "option": 0,
        "amount": "1",
        "price": "20000.34",
        "stop_price": "60000.11",
        "source": "missing access_id",
        "offset": offset,
        "limit": limit
    },
    {
        "access_id": ACCESS_ID,
        "side": 2,
        "option": 0,
        "amount": "1",
        "price": "20000.34",
        "stop_price": "60000.11",
        "source": "missing market",  # 缺少 market
        "offset": offset,
        "limit": limit
    },
    {
        "access_id": ACCESS_ID,
        "market": "BTCUSDT",
        "option": 0,
        "amount": "1",
        "price": "20000.34",
        "stop_price": "60000.11",
        "source": "missing side",  # 缺少 side
        "offset": offset,
        "limit": limit
    },
    # 字段长度限制
    {
        "access_id": ACCESS_ID,
        "market": "BTCUSDT",
        "side": 1,
        "option": 0,
        "amount": "1",
        "price": "20000.34",
        "stop_price": "60000.11",
        "source": "a" * 31,  # 超过 30 个字节
        "offset": offset,
        "limit": limit
    },
    {
        "access_id": ACCESS_ID,
        "market": "BTCUSDT",
        "side": 1,
        "option": 0,
        "amount": "1",
        "price": "20000.34",
        "stop_price": "60000.11",
        "source": "short",  # 合法长度
        "offset": offset,
        "limit": limit
    },

    # 非法值
    {
        "access_id": ACCESS_ID,
        "market": "INVALID_MARKET",  # 不存在的市场
        "side": 2,
        "option": 0,
        "amount": "1",
        "price": "20000.34",
        "stop_price": "60000.11",
        "source": "Invalid market test",
        "offset": offset,
        "limit": limit
    },
    {
        "access_id": ACCESS_ID,
        "market": "BTCUSDT",
        "side": 2,
        "option": 0,
        "amount": "-1",  # amount 为负数
        "price": "20000.34",
        "stop_price": "60000.11",
        "source": "Negative amount test",
        "offset": offset,
        "limit": limit
    },
    {
        "access_id": ACCESS_ID,
        "market": "BTCUSDT",
        "side": 2,
        "option": 0,
        "amount": "1",
        "price": "-20000.34",  # price 为负数
        "stop_price": "60000.11",
        "source": "Negative price test",
        "offset": offset,
        "limit": limit
    },
    {
        "access_id": ACCESS_ID,
        "market": "BTCUSDT",
        "side": 2,
        "option": 0,
        "amount": "1",
        "price": "20000.34",
        "stop_price": "-60000.11",  # stop_price 为负数
        "source": "Negative stop price test",
        "offset": offset,
        "limit": limit
    },
    {
        "access_id": ACCESS_ID,
        "market": "ETHUSDT",
        "side": 1,
        "option": 1,
        "amount": "0.5",
        "price": "3000.50",
        "stop_price": "4000.00",
        "source": "Valid source",
        "offset": offset,
        "limit": 10000 # limit超出100最大值
    }
]

put_market = [
    # 正常场景
    {
        "access_id": ACCESS_ID,
        "market": "BTCUSDT",
        "side": 1,
        "amount": "1000",
        "option": 0,
        "source": "U买B"
    },
    {
        "access_id": ACCESS_ID,
        "market": "BTCUSDT",
        "side": 2,
        "amount": "0.1",
        "option": 0,
        "source": "B买U"
    },
    {
        "access_id": ACCESS_ID,
        "market": "BTCUSDT",
        "side": 1,
        "amount": "0.5",
        "option": 8,
        "source": "限价买入"
    },
    {
        "access_id": ACCESS_ID,
        "market": "BTCUSDT",
        "side": 2,
        "amount": "0.2",
        "option": 16,
        "source": "限价卖出"
    },
    {
        "access_id": ACCESS_ID,
        "market": "ETHUSDT",
        "side": 1,
        "amount": "1.0",
        "option": 0,
        "source": "ETH买入"
    },
    {
        "access_id": ACCESS_ID,
        "market": "LTCUSDT",
        "side": 2,
        "amount": "0.5",
        "option": 0,
        "source": "LTC卖出"
    },

    # 异常场景
    {
        "access_id": ACCESS_ID,
        "market": "BTCUSDT",
        "side": 1,
        "amount": "1000",
        "option": 0,
        "source": "",  # 缺少source
    },
    {
        "access_id": ACCESS_ID,
        "market": "BTCUSDT",
        "side": 1,
        "amount": "-1000",  # 委托数量为负
        "option": 0,
        "source": "U买B"
    },
    {
        "access_id": ACCESS_ID,
        "market": "BTCUSDT",
        "side": 1,
        "amount": "1000",
        "option": 0,
        "source": "AAA",
    },
    {
        "access_id": ACCESS_ID,
        "market": "INVALID_MARKET",  # 市场名称无效
        "side": 1,
        "amount": "1000",
        "option": 0,
        "source": "U买B"
    },
    {
        "access_id": ACCESS_ID,
        "market": "BTCUSDT",
        "side": 1,
        "amount": "0.1",
        "option": 0,
        "source": "a" * 31,  # source 超过 30 个字节
    },
    {
        "access_id": ACCESS_ID,
        "market": "BTCUSDT",
        "side": 1,
        "amount": "1000",
        "option": 0,
        "source": "U买B",
    },
    {
        "access_id": ACCESS_ID,
        "market": "BTCUSDT",
        "side": 2,
        "amount": "0.1",
        "option": 8,
        "source": "B买U"
    },
    {
        "access_id": ACCESS_ID,
        "market": "BTCUSDT",
        "side": 2,
        "amount": "0.00005",  # 较小的委托数量
        "option": 0,
        "source": "小额卖出"
    },
    {
        "access_id": ACCESS_ID,
        "market": "BTCUSDT",
        "side": 2,
        "amount": "10000000",  # 较大的委托数量
        "option": 0,
        "source": "大额卖出"
    },
]

put_limit = [
    # 正常场景
    {
        "access_id": ACCESS_ID,
        "market": "BTCUSDT",
        "side": 1,
        "option": 0,
        "amount": "1000",
        "price": "20000",
        "source": "U买B"
    },
    {
        "access_id": ACCESS_ID,
        "market": "BTCUSDT",
        "side": 2,
        "option": 0,
        "amount": "0.1",
        "price": "80000",
        "source": "B买U"
    },
    {
        "access_id": ACCESS_ID,
        "market": "BTCUSDT",
        "side": 1,
        "option": 8,
        "amount": "0.5",
        "price": "25000",
        "source": "限价买入"
    },
    {
        "access_id": ACCESS_ID,
        "market": "BTCUSDT",
        "side": 2,
        "option": 16,
        "amount": "0.2",
        "price": "85000",
        "source": "限价卖出"
    },
    {
        "access_id": ACCESS_ID,
        "market": "BTCUSDT",
        "side": 1,
        "option": 0,
        "amount": "1000",
        # 缺少price
        "source": "U买B"
    },
    {
        "access_id": ACCESS_ID,
        "market": "BTCUSDT",
        "side": 1,
        "option": 0,
        "amount": "-1000",  # 委托数量为负
        "price": "20000",
        "source": "U买B"
    },
    {
        "access_id": ACCESS_ID,
        "market": "BTCUSDT",
        "side": 1,
        "option": 0,
        "amount": "1000",
        "price": "-20000",  # 价格为负
        "source": "AAA"
    },
    {
        "access_id": ACCESS_ID,
        "market": "INVALID_MARKET",  # 市场名称无效
        "side": 1,
        "option": 0,
        "amount": "BBB",  # 非法数量
        "price": "20000",
        "source": "U买B"
    },
    {
        "access_id": ACCESS_ID,
        "market": "BTCUSDT",
        "side": 1,
        "option": 0,
        "amount": "0.1",
        "price": "20000",
        "source": "a" * 31,  # source 超过 30 个字节
    },
    {
        "access_id": ACCESS_ID,
        "market": "BTCUSDT",
        "side": 1,
        "option": 0,
        "amount": "0.1",
        "price": "20000",
        "source": "a" * 30,  # source 正好 30 个字节
    },
    {
        "access_id": ACCESS_ID,
        "market": "BTCUSDT",
        "side": 1,
        "option": 0,
        "amount": "1000",
        "price": "20000",
        "source": "U买B",
        # 缺少tm
    },
    {
        "access_id": ACCESS_ID,
        "market": "BTCUSDT",
        "side": 2,
        "option": 8,  # 使用不同的option
        "amount": "0.1",
        "price": "80000",
        "source": "B买U"
    },
    {
        "access_id": ACCESS_ID,
        "market": "BTCUSDT",
        "side": 2,
        "option": 0,
        "amount": "0.00005",  # 较小的委托数量
        "price": "90000",
        "source": "小额卖出"
    },
    {
        "access_id": ACCESS_ID,
        "market": "BTCUSDT",
        "side": 2,
        "option": 0,
        "amount": "10000000",  # 较大的委托数量
        "price": "75000",
        "source": "大额卖出"
    },
    {
        "market": "BTCUSDT",  # 缺少 access_id
        "side": 1,
        "option": 0,
        "amount": "1000",
        "price": "20000",
        "source": "U买B"
    },
    {
        "access_id": ACCESS_ID,
        "side": 1,
        "option": 0,
        "amount": "1000",
        "price": "20000",
        "source": "U买B",
        # 缺少 market
    },
    {
        "access_id": ACCESS_ID,
        "market": "BTCUSDT",
        "option": 0,
        "amount": "1000",
        "price": "20000",
        "source": "U买B",
        # 缺少 side
    },
    {
        "access_id": ACCESS_ID,
        "market": "BTCUSDT",
        "side": 1,
        "option": 0,
        "amount": "1000",
        # 缺少 price
        "source": "U买B"
    },
    {
        "access_id": ACCESS_ID,
        "market": "BTCUSDT",
        "side": 1,
        "option": 0,
        "amount": "1000",
        "price": "20000",
        # 缺少 source
    },
]


order_cancel = [
    {
    "access_id": ACCESS_ID,
    "market": "BTCUSDT"
}
]

order_pending= [
    {
    "access_id": ACCESS_ID,
    "market": "BTCUSDT",
    "side": 0,
    "offset": offset,
    "limit": limit

},
{
    "access_id": ACCESS_ID,
    "market": "BTCUSDT",
    "side": 1,
    "offset": offset,
    "limit": limit

},
{
    "access_id": ACCESS_ID,
    "market": "BTCUSDT",
    "side": 2,
    "offset": offset,
    "limit": limit

},
    {
    "access_id": ACCESS_ID,
    "market": "XRPUSDT",
    "side": 0,
    "offset": offset,
    "limit": limit

},
{
    "access_id": ACCESS_ID,
    "market": "ETHUSDT",
    "side": 1,
    "offset": offset,
    "limit": limit

},
{
    "access_id": ACCESS_ID,
    "market": "TRXUSDT",
    "side": 2,
    "offset": offset,
    "limit": limit

},
{
    "access_id": ACCESS_ID,
    "market": "TRXUSDT",
    "side": 2,
    "offset": offset,
    "limit": 1000 #limit超出最大数量

},
{
    "access_id": ACCESS_ID,
    "market": "AAA0USDT", # 产品不存在
    "side": 0,
    "offset": offset,
    "limit": 100

},
{
    "access_id": ACCESS_ID,
    "market": "BTCUSDT",
    "side": 9, # 方向不存在
    "offset": offset,
    "limit": 100

}
]

cancel_allorder = [
    {
    "access_id": ACCESS_ID,
    "market": "BTCUSDT",
    "side": 0
},
{
    "access_id": ACCESS_ID,
    "market": "BTCUSDT",
    "side": 1
},
{
    "access_id": ACCESS_ID,
    "market": "BTCUSDT",
    "side": 2
},
{
    "access_id": ACCESS_ID,
    "market": "XRPUSDT",
    "side": 0
},
{
    "access_id": ACCESS_ID,
    "market": "XRPUSDT",
    "side": 9
},
{
    "access_id": ACCESS_ID,
    "market": "ETHUSDT",
    "side": 2
},
{
    "access_id": ACCESS_ID,
    "market": "ETHUSDT",
    "side": -2
}
]

#
#
# stop_limit = [
#     {
#     "access_id": ACCESS_ID,
#     "market": "BTCUSDT",
#     "side": 2,
#     "amount": "0.01",
#     "price": "63368.11",
#     "stop_price": "61182.11",
#     "source": "android"
# }
# ]