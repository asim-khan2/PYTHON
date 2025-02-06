emp = {321 : 62, 674 : 70, 743 : 80}
emp1 = {222 : 67, 672 : 90}

#update method 
emp.update(emp1)
print(emp)

for key , value in emp.items():
    print(key, value)

# clear method clear the dictionary
emp1.clear()
# print(emp1)

# pop method to use pop value or key

emp.pop(321)# pop the 321 key and value from the dictionary
print(emp)

# popitem pop the key value from the last
emp.popitem()
# print(emp)

# # del method delete the dictionary
# del emp1
# print(emp1)