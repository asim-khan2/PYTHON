cities = {"Tokyo", "Madrid", "Berlin", "Delhi"}
cities2 = {"Tokyo", "Seoul", "Kabul", "Madrid"}

#symmetric difference b/w to set or more
cities3 = cities.symmetric_difference(cities2)
print(cities3)

# add method add the value in the set
cities.add("Amroha")
print(cities)

#remove/dicard method to use the remove the element from the set
cities.remove("Amroha")
# cities.discard("Amroha")
print(cities)

# pop method return the pop item and pop random item
item = cities.pop()
print(cities)
print(f"poped item is {item}")

#clear method clear all item from the set 
cities.clear()
print(cities)