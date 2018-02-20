#!/usr/bin/python3

import numpy as np
import matplotlib.pyplot as plt
import requests
import json
import ipdb

#Returns vectors of operations/time
def getLastOperations(pair):
	payload = {'pair' : pair}
	r = requests.get("https://api.kraken.com/0/public/OHLC", params=payload)
	data = json.loads(r.text)
	A = np.array(data['result']['XXBTZEUR'])
	#ipdb.set_trace()
	return A[:,0:2]
	#time = A[:,0]
	#open_value = A[:,1]
	#ipdb.set_trace()

operations = getLastOperations('BTCEUR')

plt.plot(operations[:,0], operations[:,1]) 
plt.show() 
