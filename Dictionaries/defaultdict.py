from collections import defaultdict
import random

dd = defaultdict(lambda: 0)
random.seed(0)
data = [random.randint(1, 5) for _ in range(10000)]
for number in data:
    dd[number] += 1

# dd['a'] = "test"
print(dd)
#
# d = dict(dd)
# print(d)