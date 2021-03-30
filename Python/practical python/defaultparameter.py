def powernum(number,pow=1):
    power = number ** pow
    return power

# Display 9 because second parameter incase of non availibity is 1 by default
print(powernum(9))   
# Display 81 because second parameter is 2 replaced default parameter
print(powernum(9,2))