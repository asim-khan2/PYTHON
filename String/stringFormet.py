letter = "My name is {1} and i am from {0}"
name = "Asim Khan"
contry = "India"

# print(letter.format(name, contry))
print(letter.format(contry,name))

# optimized by the pyhon after update 3.6

print(f"My name is {name} and I am from {contry}")

# if i need to print {name} not a value of vatiable

print(f"My name is {{name}} and I am from {{contry}}")
