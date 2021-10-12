#!/usr/bin/python3

""" Prints 2 new lines after ., ? and : """


def text_indentation(text):
    """ determins if text is str or not and print new lines"""
    
    if type(text) != str:
        raise TypeError("text must be a string")
    for i in text:
        if i == " " and flag == 1:
            continue
        if i == '.' or i == '?' or i == ":":
            print("{}{}".format(i, '\n'))
            flag = 1
        else:
            print(i, end="")
            flag = 0
