colours = ["Red", "Green", "Yellow", "Blue", "Orange"]
print(type(colours))
print(colours)
print(colours[0])
print(colours[1])
print(colours[2])
print(colours[3])
print(colours[4])

print(colours[:-1])
print(colours[-2:])

colours.append("Perpule")
print("After adding one more colour")
print(colours)

colours.remove("Green")
print(f"After remove Green colour \n\t{colours}")
colours.pop(1)
print(f"Pop element at index 1\t{colours}")

for i in colours:
    print(i)
print(len(colours))
if "Green" in colours:
    print("Green in the list")
if "Pink" in colours:
    print("Pink in the list")
else:
    print("Pink is not in the list")

print("\t",colours)
colours.sort()
print("\t",colours)
    