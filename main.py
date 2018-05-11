#!/usr/bin/python3

import matplotlib.pyplot as plt
import numpy as np
import ipdb
import krakenPublicAPI as KPAPI
import metricComputer as MComp

from sklearn.neural_network import MLPRegressor

def main():
	timeVsSellValues = KPAPI.getLastOperationsFromTradesInfos('XXBTZEUR')
	EMA = MComp.ComputeEMA(timeVsSellValues)
	timeVsSellValuesBis=timeVsSellValues.astype(np.float64)
	#ipdb.set_trace()
	reg = MLPRegressor(hidden_layer_sizes=(50,))
	#Training on first 999 samples
	reg.fit(timeVsSellValuesBis[:999,0].reshape(-1, 1),timeVsSellValuesBis[:999,1].reshape(-1, 1))

	#Predicting next 1 samples
	predict=reg.predict(timeVsSellValuesBis[-1:,0].reshape(-1, 1))

	#ipdb.set_trace()

	plt.figure(1)
	ax = plt.subplot(211)
	ax.set_title("BTCEUR vs TIME")
	plt.plot(timeVsSellValuesBis[:,0], timeVsSellValuesBis[:,1])

	ax = plt.subplot(212)
	ax.set_title("EMA(BTCEUR vs TIME)")
	plt.plot(timeVsSellValuesBis[:,0], EMA[:], 'r--')
	plt.show()
 

if __name__ == "__main__":
	# execute only if run as a script
	main()




