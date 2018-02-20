import pandas as PD
import numpy as NP
import ipdb

def ComputeMA(data):
	#moving average
	D = PD.Series(data[:,1])
	return D.rolling(center=False,window=10).mean()
	#ipdb.set_trace()

def ComputeEMA(data):
	#Exponential moving average
	D = PD.Series(data[:,1])
	return PD.ewma(D,0.99)
	#ipdb.set_trace()


