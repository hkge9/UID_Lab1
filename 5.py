def max_dct(*dicts):
    result = {}
    for d in dicts:
        for key, value in d.items():
            if key in result:
                result[key] = max(result[key], value)
            else:
                result[key] = value
    return result

def sum_dct(*dicts):
    result = {}
    for d in dicts:
        for key, value in d.items():
            if key in result:
                result[key] += value
            else:
                result[key] = value
    return result

dict1 = {'a': 5, 'b': 3, 'c': 10}
dict2 = {'a': 9, 'b': 1, 'd': 7}
dict3 = {'a': 4, 'c': 2, 'e': 8}


print(max_dct(dict1, dict2, dict3))

print(sum_dct(dict1, dict2, dict3))