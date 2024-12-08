empty_set = set()

print(empty_set)

elements_set = {1, 6, 2, 3, 4, 8, 5}

print(elements_set)

my_set = set()

my_set.add(1)
my_set.add(5)
my_set.add(8)

print(my_set)

set_g = elements_set - my_set
print(set_g)

set_g.clear()
print(set_g)

set_k = my_set.copy()
print(set_k)