#author: 半熟的韭菜

from websocket import create_connection
import websocket
import gzip
import time
import json

from pymongo import MongoClient

if __name__ == '__main__':
    while(True):
        try:
            ws = create_connection("wss://api.huobipro.com/ws")
            break
        except:
            print('connect ws error,retry...')


    conn = MongoClient('localhost', 27017)
    db = conn.price_history

    # 价格流
    tradeStr="""{"sub": "market.ltcusdt.trade.detail","id": "id10"}"""
    ws.send(tradeStr)
    while(True):
        compressData=ws.recv()
        result=gzip.decompress(compressData).decode('utf-8')
        print(result[:13])
        if result[:7] == '{"ping"':
            ts=result[8:21]
            pong='{"pong":'+ts+'}'
            ws.send(pong)
            ws.send(tradeStr)

        elif result[:8]=="{'id': 'id10'":
            continue;
        else:
            print(type(result))


            data = json.loads(result)
            print(data)
            data['tick']['data']['id'] = float(data['tick']['data']['id'])



            db.col.insert(data)
            print(data)
