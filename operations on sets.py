my_set = {1,2,2,3,4,4,4,4}
print("set:",my_set)
my_set.add(5)
print("set:", my_set)
set1 = my_set
set2 = {4,5,6,7}
print("\nset 1", set1)
print('set2:' , set2)
print("Difference")
print(set1.difference(set2))
print("symmetric Difference")
print(set1.symmetric_difference(set2))