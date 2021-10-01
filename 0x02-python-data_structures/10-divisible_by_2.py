#!/usr/bin/python3
def divisible_by_2(my_list=[]):
    if not my_list:
        return None
    flag = list(my_list)
    for x in range(len(my_list)):
        if my_list[x] % 2 == 0:
            flag[x] = True
        else:
            flag[x] = False
    return flag
