from common.config import ACCESS_ID,offset,limit
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
        "business": 0,
        "offset": offset,
        "limit": limit,
    }
]

market_detail = [{
        "market": "BTCUSDT",
    }
]

market_kline = [{
        "market": "BTCUSDT",
        "interval": 60,
    }
]
market_depth = [{
        "market": "BTCUSDT",
        "limit": 5,
        "merge": 0.001
    }
]
