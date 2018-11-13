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
    db = conn.ltcusdt
    # 价格流
    tradeStr="""{"sub": "market.ltcusdt.trade.detail","id":"id1"}"""
    ws.send(tradeStr)
    while(True):
        compressData=ws.recv()
        result=gzip.decompress(compressData).decode('utf-8')
        if result[:7] == '{"ping"':
            ts=result[8:21]
            pong='{"pong":'+ts+'}'
            ws.send(pong)
            ws.send(tradeStr)
        else:
            data = json.loads(result)
            if 'id' not in data:
                #data['tick']['data']['id'] = float(data['tick']['data']['id'])
                for i,value in enumerate(data['tick']['data']):
                    data['tick']['data'][i]['id']=float(data['tick']['data'][i]['id'])
                db.price_history.insert(data)

