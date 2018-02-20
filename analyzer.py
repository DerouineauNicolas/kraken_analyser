#!/usr/bin/python3

import numpy as np
import matplotlib.pyplot as plt
import requests
import json
import ipdb

payload = {'pair' : 'BTCEUR'}
r = requests.get("https://api.kraken.com/0/public/OHLC", params=payload)
data = json.loads(r.text)
A = np.array(data['result']['XXBTZEUR'])
time = A[:,0]
open_value = A[:,1]
#ipdb.set_trace()
plt.plot(time, open_value) 
plt.show() 
