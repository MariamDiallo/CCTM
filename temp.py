# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""

import gdax
import numpy as np
import matplotlib.pyplot as plt
import time
import plotly
import plotly.plotly as py
import plotly.graph_objs as go




public_client = gdax.PublicClient()
LTC_EUR_Live = public_client.get_product_order_book('LTC-EUR')
#print(get_bid(BTC_USD_Live.get("bids")))
bid_LTC_EUR = float(LTC_EUR_Live.get("bids")[0][0])
ask_LTC_EUR = float(LTC_EUR_Live.get("asks")[0][0])

BTC_EUR_Live = public_client.get_product_order_book('BTC-EUR')
#print(get_bid(BTC_USD_Live.get("bids")))
bid_BTC_EUR = float(BTC_EUR_Live.get("bids")[0][0])
ask_BTC_EUR = float(BTC_EUR_Live.get("asks")[0][0])

BTC_LTC_Live = public_client.get_product_order_book('LTC-BTC')
#print(get_bid(BTC_USD_Live.get("bids")))
bid_BTC_LTC = float(BTC_LTC_Live.get("bids")[0][0])
ask_BTC_LTC = float(BTC_LTC_Live.get("asks")[0][0])

print(-ask_BTC_EUR + bid_LTC_EUR/ask_BTC_LTC )
print(+ bid_BTC_EUR - ask_LTC_EUR/bid_BTC_LTC )
list1 = []
list2 = []
axis = []
x = 0
while x < 100:
    LTC_EUR_Live = public_client.get_product_order_book('LTC-EUR')
    #print(get_bid(BTC_USD_Live.get("bids")))
    bid_LTC_EUR = float(LTC_EUR_Live.get("bids")[0][0])
    ask_LTC_EUR = float(LTC_EUR_Live.get("asks")[0][0])
    BTC_EUR_Live = public_client.get_product_order_book('BTC-EUR')
    #print(get_bid(BTC_USD_Live.get("bids")))
    bid_BTC_EUR = float(BTC_EUR_Live.get("bids")[0][0])
    ask_BTC_EUR = float(BTC_EUR_Live.get("asks")[0][0])
    BTC_LTC_Live = public_client.get_product_order_book('LTC-BTC')
    #print(get_bid(BTC_USD_Live.get("bids")))
    bid_BTC_LTC = float(BTC_LTC_Live.get("bids")[0][0])
    ask_BTC_LTC = float(BTC_LTC_Live.get("asks")[0][0])
    list1.append(-ask_BTC_EUR + bid_LTC_EUR/ask_BTC_LTC )
    list2.append( bid_BTC_EUR - ask_LTC_EUR/bid_BTC_LTC)
    time.sleep(10)
    axis.append(x)
    x += 1



# evenly sampled time at 200ms intervals


# red dashes, blue squares and green triangles
print(list1)
print(list2)

plt.plot(axis, list1, 'g^', axis, list2, 'bs',)
plt.axis([-0.5, max(axis) + 0.5 , min(min(list1), min(list2)) - 5, max(max(list1),max(list2))+5])
plt.show()
















