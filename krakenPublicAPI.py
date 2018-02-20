#!/usr/bin/python3

import numpy as np
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
	#ipdb.set_trace()


