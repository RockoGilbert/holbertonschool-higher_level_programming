#!/usr/bin/python3
def divisible_by_2(my_list=[]):
    if not my_list:
        return None
    new = list(my_list)
    for x in range(len(my_list)):
        if my_list[x] % 2 == 0:
            new[x] = True
        else:
            new[x] = False
            return flag
