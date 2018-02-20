#!/usr/bin/python3

import matplotlib.pyplot as plt
import numpy as np
import ipdb
import krakenPublicAPI as KPAPI
import metricComputer as MComp

def main():
	timeVsSellValues = KPAPI.getLastOperationsFromTradesInfos('XXBTZEUR')
	EMA = MComp.ComputeEMA(timeVsSellValues)
	timeVsSellValuesBis=timeVsSellValues.astype(np.float64)
	ipdb.set_trace()

	plt.figure(1)
	ax = plt.subplot(211)
	ax.set_title("BTCEUR vs TIME")
	plt.plot(timeVsSellValuesBis[:200,0], timeVsSellValuesBis[:200,1])

	ax = plt.subplot(212)
	ax.set_title("EMA(BTCEUR vs TIME)")
	plt.plot(timeVsSellValuesBis[:200,0], EMA[:200], 'r--')
	plt.show()
 

if __name__ == "__main__":
	# execute only if run as a script
	main()




