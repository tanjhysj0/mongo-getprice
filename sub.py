from websocket import create_connection
import websocket
import gzip
import time
import json

from pymongo import MongoClient

class price:
    #连接
    def connect(self):
        while(True):
            try:
                self.ws = create_connection("wss://api.huobipro.com/ws")
                print("连接成功")
            except:
                print('连接失败，重连中...')
                time.sleep(1)
    #订阅
    def sub_trade(self):
        self.connect()
        tradeStr="""{"sub": "market.ltcusdt.trade.detail","id":"id1"}"""
        self.ws.send(tradeStr)
    def run(self):
        conn = MongoClient('localhost', 27017)
        db = conn.ltcusdt
        # 价格流
        self.sub_trade()
        while (True):
            try:
                compressData = self.ws.recv()
                result = gzip.decompress(compressData).decode('utf-8')
            except:
                print('网络可能连接失败,重新连接')
                self.sub_trade()
            if result[:7] == '{"ping"':
                ts = result[8:21]
                pong = '{"pong":' + ts + '}'
                self.ws.send(pong)
            else:
                data = json.loads(result)
                if 'id'  in data:
                    continue
                for i, value in enumerate(data['tick']['data']):
                    data['tick']['data'][i]['id'] = float(data['tick']['data'][i]['id'])
                db.price_history.insert(data)
                print("执行到位")

if __name__ == '__main__':
    price().run()




