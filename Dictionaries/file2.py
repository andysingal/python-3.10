d = {'a': 1, 'b': 2, 'c': 3}
d['b'] = 200
print(d)

d1 = {'a': 1, 'b': 2}
d1.update(b=20, c=30)
print(d1)

d2 = {'a': 1, 'b': 2}
d2.update((k,ord(k)) for k in 'python')
print(d2)

l1 = [1, 2, 3]
l2 = 'abc'
l = (*l1, *l2)
print(l)
