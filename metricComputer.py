import pandas as PD
import numpy as NP
import ipdb

def ComputeMA(data):
	#Exponential moving average
	D = PD.Series(data[:,0], data[:,1])
	d_mva = PD.rolling_mean(D, 10)

def ComputeEMA(data):
	#Exponential moving average
	D = PD.Series(data[:,0], data[:,1])

