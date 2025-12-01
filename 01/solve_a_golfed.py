#!/usr/bin/python3
d=50;z=0
for l in open(0):d+=int(l[1:])*(l>'P'or-1);d%=100;z+=d<1
print(z)
