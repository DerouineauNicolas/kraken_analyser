#!/usr/bin/python3

import matplotlib.pyplot as plt
import numpy as np
import ipdb
import krakenPublicAPI as KPAPI

operations = KPAPI.getLastOperationsFromTradesInfos('XXBTZEUR')

#ipdb.set_trace()
plt.plot(operations[:200,1]) #Plots ops from the last 200 minutes
plt.show() 
