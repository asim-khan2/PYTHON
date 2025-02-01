# function for calculating factorial 
def factorial(n):
    if(n==0 or n==1):
        return 1
    return n*factorial(n-1) # return result

n = int(input("Enter number for calculate Factorial : "))

res = factorial(n) #function call. 

print(f"{n} factorial is {res}")