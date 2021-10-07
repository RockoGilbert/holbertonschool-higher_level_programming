def roman_to_int(roman_string):
    vals = {"I": 1, "V": 5, "X": 10, "L": 50, "C": 100, "D": 500, "M": 1000}
    total = 0
    if type(roman_string) == str:
        j = iter(list(roman_string[1:]))
        for i in roman_string:
           k = next(j, i)
           try:
               check = vals[i] < vals[k]
           except KeyError:
               return 0
           finally:
               if check:
                   total -= vals[i]
               else:
                   total += vals[i]
                   
    return total
