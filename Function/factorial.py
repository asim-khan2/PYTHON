def factorial(num):
    fac = 1
    for i in range(1,num+1):
        fac *= i
    return fac

num = int(input("Enter the number for calculate the factorial: "))
print(f"Factorial of {num} is {factorial(num)}")
