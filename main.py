#import
import discord
import websocket, json

#lists

closes, highs, lows, = [], [], [] 

#defines

def on_message(ws, message):
    json_message = json.loads(message)
    candle = json_message['k']
    is_candle_closed = candle['x']
    closed = candle['c']
    high = candle['h']
    low =  candle['l']
    vol = candle['v']
    if is_candle_closed:
        closes.append(float(closed))
        highs.append(float(high))
        lows.append(float(low))

    print(closes)
    print(highs)
    print(lows)



def on_close(ws):
    print("### Closed ###")

#start up
cc = 'btcusd'
interval = '1m'

socket = f'wss://stream.binace.com:9443/ws/{cc}t@kline_{interval}'
ws = websocket.WebSocketApp(socket,on_message= on_message, on_close= on_close)








#client = discord.Client()

#@client.event
#async def on_ready():
    #print(f'{client.user} has connected to Discord successfully!')











#DON'T TOUCH UNLESS YOUR CHANGING THE TOKEN

#client.run('') #replace token with your own token