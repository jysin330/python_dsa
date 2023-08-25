def recursion(n):
    if n > 0:
        recursion(n-1)
        recursion(n-1)
        print("woo", n)


recursion(3)
