class Person:
    def __init__(self,name,age):
        self.name = name
        self.age = age

    def __repr__(self):
        return f'Person(name={self.name}, age={self.age})'

    def __eq__(self,other):
        if isinstance(other,Person):
            return self.name == other.name and self.age == other.age
        else:
            return False

    def __hash__(self):
        print ('__hash__ called...')
        return hash((self.name, self.age))

p1 = Person('John', 78)
p2 = Person('John', 78)

print(hash(p1)), print(hash(p2))
print(p1==p2)
"""
When we call the hash() function, although it in turn calls the __hash__ method, it does something more.

It will truncate the integer returned by __hash__ to a certain width which is implementation dependent.

In my case, I can see that hashes will be truncated to 64-bits:
"""


class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __repr__(self):
        return f'({self.x}, {self.y})'

    def __eq__(self, other):
        if isinstance (other, tuple) and len(other) == 2:
            other = Point (*other)
        if isinstance (other, Point):
            return self.x == other.x and self.y == other.y
        else:
            return False

    def __hash__(self):
        return hash ((self.x, self.y))

points = {Point(0,0): 'origin', Point(1,1): 'pt at (1,1)'}
for k, v in points.items():
    print(k, v)
