#!/usr/local/bin/python2.7
    
import math;    
num=2000000;

binArray= [True]*(num+1);

def wipeMultiples(myNum, myList):
  for i in range(myNum*2,num+1,myNum):
    myList[i]=False;

for i in range(2, math.trunc(math.sqrt(num))+1):
  wipeMultiples(i,binArray);

def add(x,y): return x+y
print reduce(add, [x for x in range(2,num+1) if binArray[x]]);