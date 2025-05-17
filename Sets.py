my_set = {1,2,3}
print(f"Set of common data type: {my_set}")

my_set = {1.0, "Hello", (1, 2, 3)}
print(f"Set with fixed data type: {my_set}")

unique = {1, 5, 1, 5, 2, 1, 5, 3}
print(f"Sets are unique: {unique}")

print(f"Converting a listto a set: The list: {[1, 2, 3]} and converted set is = {set([1, 2, 3])}")

num_set = {1, 2, 3, 4, 5}
print(f"Original set = {num_set}")
num_set.pop()
print(f"The shortened set = {num_set}")

a = {-2, -4, -55, 10, 0}
b = {0, 10, 20, 99, 31}

print(f"The Union of set a and set b is = {a.union(b)}")
print(f"The Intersection of set a and set b is = {a.intersection(b)}")