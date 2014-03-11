#!/usr/local/bin/python2.7
import sys
import math
def NthPrime(num):
	pnos=[2]
	piter=1
	i=3
	while(len(pnos)<num):
		prime=True
		for x in pnos:
			if(x>math.sqrt(i)):
				break;
			if(i%x==0):
				prime=False;
		if(prime):
			pnos.append(i)
		i+=2
	return pnos[-1]
if(__name__=='__main__'):
	print NthPrime(int((sys.argv)[1]))
