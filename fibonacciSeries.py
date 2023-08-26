def fun(n):
    if n == 0 or n == 1:
        return n
    else:
        return fun(n-2) + fun(n-1)


count = 6
if count <= 0:
    print("please enter greater than 0")
else:
    for i in range(count):
        print(fun(i), end=" ")
