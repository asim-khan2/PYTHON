def n_numSum(n):
    if(n==1):
        return 1
    return n + n_numSum(n-1)

n = int(input("Enter number for the sum : "))
print("Sum is : ", n_numSum(n))