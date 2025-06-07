# `|` merges dicts. `dict2` values overwrite `dict1` if keys clash.

dict_1 = {
    'a' : 3,
    'b' : 1,
    'c' : 4,
    'd' : 2
}

dict_2 = {
    'c' : 5,
    'd' : 9,
    'e' : 6,
    'f' : 7
}

merged_dict = dict_1 | dict_2
print(merged_dict)