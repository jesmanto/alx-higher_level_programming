#!/usr/bin/python3
def no_c(my_string):
    str_arr = my_string.split()
    new_str = [s for s in my_string if s != "c" and s != "C"]
    return ''.join(new_str)
