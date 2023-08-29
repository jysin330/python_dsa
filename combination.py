def factorial(n):
    if n == 0 or n == 1:
        return 1
    else:
        return n*factorial(n-1)


n = 25
r = 3
result = factorial(n)/(factorial(r)*factorial(n-r))
print(result)
