tup = (34, 53, 44, 12,3,3, "Asim", "Asim", "asim")
print("Befor change tuple is \t\t", tup)
list = list(tup)
print(type(tup))
print(type(list))
list.append("Khan")
print("Befor pop from the list is \t\t",list)
list.reverse()
print("list after reversed \n\t", list)
list.pop(0)
print("After pop from the list is \t\t",list)
tup = tuple(list)
print("After change tuple is \t\t", tup)

tup1 = (3,5, 34,)
print(tup+tup1)

print("\n\t",tup.count("asim"))

print("\n\t",tup.index(44))
print("\n\t",tup.index(3,3,6))
