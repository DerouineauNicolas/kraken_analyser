#!/usr/bin/python3

import matplotlib.pyplot as plt
import numpy as np
import ipdb
import krakenPublicAPI as KPAPI
import metricComputer as MComp

def main():
	timeVsSellValues = KPAPI.getLastOperationsFromTradesInfos('XXBTZEUR')
	plt.plot(timeVsSellValues[:200,1]) #Plots ops from the last 200 minutes
	plt.show()
	MComp.ComputeEMA(timeVsSellValues)
 

if __name__ == "__main__":
    # execute only if run as a script
    main()




