# def useful_function(x: str) -> int:  # -> int hints an expected datatype as outcome
#     x = int(x)
#     # Useful code, using x, here
#     return x
#
#
# print(useful_function(5))

# Matheuebungen

def sum_FN(x):
    if x < 0:
        x = x * -1
        i = 1
        s = 0
        while i <= x:
            s = s + i
            i = i + 1
            print(s)
        s = s * -1
        return s
    else:
        i = 1
        s = 0
        while i <= x:
            s = s + i
            i = i + 1
            print(s)
        return s

print(sum_FN(-3))

# def fakul(x):
#     i = 1
#     d = x
#     while i <= x:
#         d = d * i
#         i = i + 1
#     return d
#
# print(fakul(5))
