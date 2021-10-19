#!/usr/bin/python
# -*- coding: utf-8 -*-

mylist = ["Luis", "Juan", "Carmen"]
mylist.append("Carlos")
mylist.append("Maria")
# print list
for x in mylist:
    print(x)
mylist[0]
#mylist.extends(["Luisa","Antonio"])
mylist.insert(2, "new")

for i in mylist[1:len(mylist)]:
    print(i)


