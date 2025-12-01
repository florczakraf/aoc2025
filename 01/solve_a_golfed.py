#!/usr/bin/python3
import sys;z=0;d=50
for l in sys.stdin:d+=int(l[1:])*(l>'P'or-1);d%=100;z+=d<1
print(z)
