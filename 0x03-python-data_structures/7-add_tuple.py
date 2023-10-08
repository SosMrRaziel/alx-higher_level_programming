# #!/usr/bin/python3
def add_tuple(tuple_a=(), tuple_b=()):
    tuple_1 = tuple_a + (0, 0)
    tuple_2 = tuple_b + (0, 0)
    new_tuple = (tuple_1[0] + tuple_2[0], tuple_1[1] + tuple_2[1])
    return new_tuple

# def add_tuple(tuple_a=(), tuple_b=()):
#     result = (0, 0)
#     for i in range(2):
#         if i < len(tuple_a):
#             a = tuple_a[i]
#         else:
#             a = 0
#         if i < len(tuple_b):
#             b = tuple_b[i]
#         else:
#             b = 0
#         result = result[:i] + (a + b,) + result[i+1:]
#     return result
