def half(n):
    if n == 1:
        return 2
    else:
        return half(n-1)/2

res = half(3)
print(res)
