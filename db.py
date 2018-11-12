from pymongo import MongoClient

conn = MongoClient('localhost', 27017)

db = conn.testdb
json_str = {"ch": "market.ltcusdt.trade.detail",
            "ts": 1541950729278.0,
            "tick": {"id": 27740800752, "ts": 1541950729176, "data": [
                {"amount": 2.000000000000000000, "ts": 1541950729176.0, "id": 2774080075216467551499.0
                 "price": 51.200000000000000000, "direction": "sell"},
                {"amount": 0.388800000000000000, "ts": 1541950729176.0, "id": 2774080075216467552453.0,
                 "price": 51.200000000000000000, "direction": "sell"}]}
            };

db.col.insert(json_str)
