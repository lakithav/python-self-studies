"""
my_set = {'Lakitha',20,3.15,True,20}
print(my_set)

A = {1, 2, 3, 7, 5}
B = {5, 7, 9, 11, 10}

print(A.union(B))
print(A.intersection(B))

"""

A = {'Lakitha',20,3.15,True,20}

A.add('Python')
print(A)

A.update(['Programming', 'Language'])
print(A)

A.remove('Lakitha')
print(A)

A.discard(3.15) #discard() method will not raise an error if the element is not found in the set, while remove() will raise a KeyError.
print(A)

A.pop()
print(A)