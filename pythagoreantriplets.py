#!/usr/local/bin/python2.7
    
for i in range(1,998):
  for j in range(1,999-i):
    k=1000-i-j;
    if(i*i+j*j==k*k):
      print i,j,k
      print i*j*k;