def sum(*args):
    sumall = 0
    for i in args:
        if isinstance(i,int):
            sumall += i
        else:
            sumall += 0     
    return sumall    

# Calculate and provide sum of all argument inside function argument
print(sum(9,2,5,'alpha'))