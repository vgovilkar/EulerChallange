#!/usr/local/bin/python2.7
    
import math;

numcap=2000000;

def multremover(i):
  def innerremover(x):
    if(x!=i):
      return x % i != 0;
    else:
      return True;
  return innerremover

#Eurotothenes sieve
def sieve(numlist):
  for i in numlist:
    if(i>math.trunc(math.sqrt(numcap))+1):
      break;
    numlist=filter(multremover(i), numlist);  
  return numlist;

numlist=range(2,numcap);

print "hi";
numlist=sieve(numlist);
def add(x,y): return x+y
print reduce(add, numlist);