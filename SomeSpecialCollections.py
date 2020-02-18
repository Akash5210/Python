# ChainMap
from collections import ChainMap

a = {1: 'edureka', 2: 'python'}
b = {3: 'tata', 4: 'birla'}

al = ChainMap(a, b)
print(a)
print(b)
print(al)
print("---------------------------------------------")

# counter
from collections import Counter

a = [1, 1, 2, 3, 2, 2, 4, 5, 4, 5, 4, 3, 6, 2, 2]
c = Counter(a)
print(c)
print(list(c.elements()))

print(c.most_common())
sub = {2: 1, 6: 1}
print(c.subtract(sub))
print(c.most_common())

# OrderedDict
from collections import OrderedDict

d = OrderedDict()
d[1] = 'a'
d[2] = 'k'
d[3] = 'a'
d[4] = 's'
d[5] = 'h'
print(d)

# defaultdict
# some more collections are not written





