# Find the Factorial of The given number?

mumber = int(input("Type Number: "))

def Factorial(num):
    fact = 1

    if num <= 0:
        return "Factorial does not exist for negative number"
    else:
        for x in range(1,num+1):
            fact = fact * x
        return fact


print("The Factorial of ", mumber," is ", Factorial(mumber))