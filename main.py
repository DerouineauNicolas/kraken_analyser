#!/usr/bin/python3

import matplotlib.pyplot as plt
import numpy as np
import ipdb
import krakenPublicAPI as KPAPI

def main():
	operations = KPAPI.getLastOperationsFromTradesInfos('XXBTZEUR')
	plt.plot(operations[:200,1]) #Plots ops from the last 200 minutes
	plt.show() 

if __name__ == "__main__":
    # execute only if run as a script
    main()




