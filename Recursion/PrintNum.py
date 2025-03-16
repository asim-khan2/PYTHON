def printNum(num):
    if(num == 0):
        return 0
    print(num)
    printNum(num-1)

num = int(input("Enter the number for print : "))
printNum(num)