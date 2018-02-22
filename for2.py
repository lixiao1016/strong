#!/usr/bin/python
#-*- coding:UTF-8 -*-

# 斐波那契数列

a=0
b=1
c=1
d=1
e=1.1
f=1
while b < 1000:
    print "%5d" %b,
    a, b = b, a+b
    d+=1
print("")
while c < d:   
    print "%5d" %c,
    c+=1
print("")
while f < d:
    print "%5.2f" %e,
    f+=1
    e=1.1**f
        
