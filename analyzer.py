#!/usr/bin/python3

import numpy as np
import matplotlib.pyplot as plt
import requests
import json
import ipdb

#pair: altname of pair as given in crypto infos
#Returns vectors of time/operations
def getLastOperationsFromTradesInfos(pair):
	payload = {'pair' : pair}
	r = requests.get("https://api.kraken.com/0/public/Trades", params=payload)
	data = json.loads(r.text)
	A = np.array(data['result'][pair])
	#ipdb.set_trace()
	#A = <price>, <volume>, <time>, <buy/sell>, <market/limit>, <miscellaneous>
	return np.column_stack((A[:,2],A[:,0]))
	#time = A[:,0]
	#open_value = A[:,1]
	#ipdb.set_trace()

operations = getLastOperationsFromTradesInfos('XXBTZEUR')


ipdb.set_trace()
plt.plot(operations[:,1]) #Plots ops from the last 1000 minutes
plt.show() 
