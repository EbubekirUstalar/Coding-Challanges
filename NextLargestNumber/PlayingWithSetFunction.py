my_set = {1,2,3}

print(type(my_set))

print(my_set)

m_set = {1,2,4,3,2,31,1,6}
print("m_set",m_set)

my_sett = {1.0, "Hello", (1, 2, 3)}
print(my_sett)


my_sett1 = set({1,3,2,4,4,2,3,1})
print(my_sett1)

EmptySet = set()
print(type(EmptySet))

deneme_set = set("HelloWorld")
print("set: ", deneme_set)
print("lengtht: ", len(deneme_set))

for i in range(len(deneme_set)):
    deneme_set.pop()
    print(deneme_set, "i", i, "lenght", len(deneme_set))


A_set = {1, 2, 3, 4, 5}
B_set = {4, 5, 6, 7, 8}

print(A_set | B_set)    # union
print(A_set.union(B_set))
print(B_set.union(A_set))

print(A_set & B_set)    # intersection
print(A_set.intersection(B_set))
print(B_set.intersection(A_set))

print(A_set - B_set)    # difference
print(B_set - A_set)    # difference
print(A_set.difference(B_set))
print(B_set.difference(A_set))


print(A_set ^ B_set)    # symmetric_difference                   same as union - intersection
print(A_set.symmetric_difference(B_set))
print(B_set.symmetric_difference(A_set))
