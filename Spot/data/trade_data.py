from common.config import ACCESS_ID,offset,limit
ACCESS = "bbf0929f-0fbb-4f87-87a7-8577bc1aa447"
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
    }
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
    }
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
}
]

order_stop_limit = [
    {
    "access_id": ACCESS_ID,
    "market": "BTCUSDT",
    "side": 2,
    "amount": "0.1",
    "price": "60000",
    "stop_price": "50000",
    "source": "TEST"
},
{
"access_id": ACCESS_ID,
"market": "BTCUSDT",
"side": 1,
"amount": "1",
"price": "60000",
"stop_price": "60000",
"source": "TEST"
}
]
order_stop_market = [
    {
    "access_id": ACCESS_ID,
    "market": "BTCUSDT",
    "side": 2,
    "amount": "1",
    "stop_price": "50000",
    "source": "TEST"
},
{
    "access_id": ACCESS_ID,
    "market": "BTCUSDT",
    "side": 1,
    "amount": "100",
    "stop_price": "49999",
    "source": "TEST"
},
{
    "access_id": ACCESS_ID,
    "market": "BTCUSDT",
    "side": 1,
    "amount": "100",
    "stop_price": "65000",
    "source": "TEST"
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