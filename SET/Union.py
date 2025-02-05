s = {2, 3, 56, 45}
s1 = {9, 1, 5, 56, 4}

print(f"Set one is {s}")
print(f"Set second is {s1}")

# using union function find the union between set s and s1
set_union = s.union(s1)
print(f"\tset union is {set_union}")

set_update = s.update(s1) #update in set s mean union both set in the one set
print(s)