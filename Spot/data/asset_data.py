from common.config import ACCESS_ID,offset,limit
# asset_query = [{
#         "access_id": ACCESS_ID
# },
# {
#         "access_id": "ASwL1pYxdoVKBY3fArMFMnBwSAS21S"
# }
# ]
asset_query = [{
        "access_id": ACCESS_ID
}
]
get_pending = [{
        "access_id": ACCESS_ID,
        "market": "BTCUSDT",
        "side": 0,
        "offset": offset,
        "limit": limit,
    }
]
asset_history = [{
        "access_id": ACCESS_ID,
        "asset": "",
        "business": "",
        "offset": offset,
        "limit": limit,
    },
    {
        "access_id": ACCESS_ID,
        "asset": "BTC",
        "business": "trade",
        "offset": offset,
        "limit": limit,
    },
    {
        "access_id": ACCESS_ID,
        "asset": "USDT",
        "business": "fee",
        "offset": offset,
        "limit": limit,
    },
    {
        "access_id": ACCESS_ID,
        "asset": "USDT",
        "business": "fee",
        "offset": offset,
        "limit": limit,
    }
]

market_detail = [{
        "market": "BTCUSDT"
    },
{
        "market": "XRPUSDT"
    },
{
        "market": "ETHUSDT"
    },
{
        "market": "LTCUSDT"
    },
{
        "market": "LCUSDT"
    }
]

market_kline = [{
        "market": "BTCUSDT",
        "interval": 60
    },
{
        "market": "XRPUSDT",
        "interval": 1
    },
{
        "market": "ETHUSDT",
        "interval": 300
    },
{
        "market": "EHUSDT",
        "interval": 1
    }
]
market_depth = [{
        "market": "BTCUSDT",
        "limit": 50,
        "merge": 0.001
    },
{
        "market": "ETHUSDT",
        "limit": 50,
        "merge": 0.1
    },
{
        "market": "XRPUSDT",
        "limit": 50,
        "merge": 0.001
    },
{
        "market": "XRUSDT",
        "limit": 50,
        "merge": 0.1
    }
]
