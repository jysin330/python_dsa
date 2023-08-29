def powerProgram(base, exp):
    if exp == 0:
        return 1
    else:
        return base * powerProgram(base, exp-1)


print(powerProgram(2, 0))
