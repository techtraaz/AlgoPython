
def pow(base,exp):
    if exp == 0:
        return 1
    return base * pow(base,exp-1)
b = int(input('base:'))
x = int(input('exponenet'))
res = pow(b,x)
print(res)


