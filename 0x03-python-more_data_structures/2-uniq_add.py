#!/usr/bin/python3
def uniq_add(my_list=[]):
    newList = []
    store = 0
    for x in my_list:
        if x not in newList:
            newList.append(x)
    for n in newList:
        store += n
    return store
