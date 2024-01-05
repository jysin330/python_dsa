def powerProgram(n,p):
    if p==0:
        return 1
    else:
        return n*powerProgram(n,(p-1))
    
print(powerProgram(2,4))