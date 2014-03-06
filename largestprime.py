#!/usr/local/bin/python2.7
    
import math;
num = 600851475143;
pnos = [2];
upper = math.trunc(math.sqrt(num));
print upper;

for i in range (3, upper, 2):
  prime=True;
  for x in pnos:
    if(i%x==0):
      prime=False;
  if(prime):
    pnos.append(i);

print(pnos[-1]);