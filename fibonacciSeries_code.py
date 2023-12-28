def fibonacci(n):
    if n<=1:
        return n
    else:
        return fibonacci(n-1)+ fibonacci(n-2)
        
i = int(input("write the nth value of fibonacci series"))

if (i<= 0):
    print("please enter number greater than 2")
else:
    for num in range(i):
        print(fibonacci(num),end=" ,")