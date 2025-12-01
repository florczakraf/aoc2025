#!/usr/bin/python3
import sys;z=0;d=50
for l in sys.stdin:r=int(l[1:]);d+=r*(l>'P'or-1);d%=100;z+=d<1
print(z)
