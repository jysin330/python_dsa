def factorial(n):
    if n >= 0:
        if n == 0 or n == 1:
            return 1

        else:
            return (n * factorial(n-1))
    else:
        return "n must be whole number"


print(factorial(-2))
