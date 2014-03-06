#!/usr/local/bin/python2.7

pnos = {2:0,3:0,5:0,7:0,11:0,13:0,17:0,19:0};

def maxprimeFactorization(num):
  for i in pnos.keys():
    times=0;
    while(num%i==0):
      times+=1;
      num=num/i;
    if(pnos[i]<times):
      pnos[i]=times;

for i in range(2,20):
  maxprimeFactorization(i);
print pnos;

product = 1;
for x in pnos.keys():
  while(pnos[x]!=0):
    product*=x;
    pnos[x]-=1;

print product;
    
