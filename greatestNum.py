num1 = int(input("Enter number first :"))
num2 = int(input("Enter number second : "))
num3 = int(input("Enter number third : "))

if(num1 > num2 and num1 > num3):
    print(f"{num1} is greatest")
elif(num2 > num1 and num2 > num3):
    print(f"{num2} is greatest")
else:
    print(f"{num3} is greatest")