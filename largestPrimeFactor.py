#!/usr/local/bin/python2.7
import sys
import math

def LargestPrimeFactor(num):
	pnos = [2];
	upper = math.trunc(math.sqrt(num))
	for i in range (3, upper, 2):
		prime=True;
		for x in pnos:
			if(i%x==0):
				prime=False;
		if(prime):
			pnos.append(i);

	return (pnos[-1]);

if(__name__=='__main__'):
	print(LargestPrimeFactor(int((sys.argv)[1])))