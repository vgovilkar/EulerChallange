#!/usr/local/bin/python2.7
    
import math;
pnos=[2];
piter=1;
i=3;
while(len(pnos)<10001):
  prime=True;
  
  for x in pnos:
    if(x>math.sqrt(i)):
      break;
    if(i%x==0):
      prime=False;
  if(prime):
    pnos.append(i);
  i+=2;

print "hello";
print pnos[-1];