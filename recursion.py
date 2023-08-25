def func(n):
    if (n > 0):
        print(f"woo {n}")  # forward tracking
        func(n-1)
        func(n-1)


        # print(f"woo {n}") #backward traacking
n = 3
func(n)
