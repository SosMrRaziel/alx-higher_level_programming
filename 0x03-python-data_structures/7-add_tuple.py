# #!/usr/bin/python3
def add_tuple(tuple_a=(), tuple_b=()):
    result = (0, 0)
    for i in range(2):
        if i < len(tuple_a):
            a = tuple_a[i]
        else:
            a = 0
        if i < len(tuple_b):
            b = tuple_b[i]
        else:
            b = 0
        result = result[:i] + (a + b,) + result[i+1:]
    return result
