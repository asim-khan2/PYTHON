cities = {"Tokyo", "Madrid", "Berlin", "Delhi"}
cities2 = {"Tokyo", "Seoul", "Kabul", "Madrid"}

print(f"\tFirst set is {cities}")
print(f"\tSecond set is {cities2}")

print("This is the intersection")
print(cities.intersection(cities2))

print("this is the cities update to the cities2 ")
cities.intersection_update(cities)
print(cities)