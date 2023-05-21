def map_func(func, var):
    return (func(x) for x in var)


def func(var):
    return var * 2


array = [1, 3, 4, 5, 6, 7]
print(map(func, array))
print(map_func(func, array))
