def fectorial(num):
    if (num == 1 or num == 0):
        return 1
    else:
        return num* fectorial(num-1)
    

i =1
fec = fectorial(i)
print(fec)