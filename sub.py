#author: 半熟的韭菜

from websocket import create_connection
import gzip
import time

if __name__ == '__main__':
    while(1):
        try:
            ws = create_connection("wss://api.huobipro.com/ws")
            break
        except:
            print('connect ws error,retry...')


    # 价格流
    tradeStr="""{"sub": "market.ltcusdt.trade.detail","id": "id10"}"""

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
            print(result)