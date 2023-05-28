a, b, *rest = range(10)
print(a, b, rest)

nested_list = [(1,2, (i, j)) for i in range(2) for j in range(3)]
print(nested_list)

for one, two, (iuri, jiuri) in nested_list:
	print(f"{one=}, {iuri=}")
	
from collections import namedtuple
City = namedtuple('City', 'name country')
tokyo = City('tokyo', 'JP')
print(tokyo.country)