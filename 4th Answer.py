it_companies = {'Facebook', 'Google', 'Microsoft', 'Apple', 'IBM', 'Oracle', 'Amazon'}
length = len(it_companies)
print(length)
it_companies.add('Twitter')
print(it_companies)
MNCS = ('Sprint', 'AcurIt', 'Cisco', 'Alphabet')
it_companies.update(MNCS)
print(it_companies)
it_companies.remove('Cisco')
print(it_companies)
##REMOVE:#It removes  element from the set if the element is present or else raises  key error.
#DISCARD:It removes element present in the set#
A = {19, 22, 24, 20, 25, 26}
B = {19, 22, 20, 25, 26, 24, 28, 27}
print(A.union(B))
print(A.intersection(B))
print(A.issubset(B))
print(A.isdisjoint(B))
print(A.union(B) & B.union(A))
print(A.symmetric_difference(B))
A.clear()
print(A)
age = [22, 19, 24, 25, 26, 24, 25, 24]
AG = len(age)
print(AG)
SG = set(age)
print(SG)
length = len(SG)
print(length)



