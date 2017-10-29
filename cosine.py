import math
from collections import Counter

def build_vector(iterable1, iterable2):
    counter1 = Counter(iterable1)
    counter2 = Counter(iterable2)
    d = counter1
    print d.keys()
    print d.values()
    print counter1
    print counter2
    all_items = set(counter1.keys()).union(set(counter2.keys()))
    print all_items
    vector1 = [counter1[k] for k in all_items]
    vector2 = [counter2[k] for k in all_items]
    print vector1
    print vector2
    return vector1, vector2, counter1, counter2

def cosim(v1, v2):
    dot_product = sum(n1 * n2 for n1, n2 in zip(v1, v2) )
    magnitude1 = math.sqrt(sum(n ** 2 for n in v1))
    magnitude2 = math.sqrt(sum(n ** 2 for n in v2))
    return dot_product / (magnitude1 * magnitude2)


l1 = "Julie loves me more than Linda loves me".split()
l2 = "Jane likes me more than Julie loves me or".split()


v1, v2, c1, c2 = build_vector(l1, l2)
print(cosim(v1, v2))
print c1
