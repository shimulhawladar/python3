# Find the number of occurrences of each vowel in the string:


w = input("Type Word: ").lower()

v = {"a":0,'e':0,'i':0,'o':0,'u':0}

result = {}

for x in w:
    if x in v.keys():
        v[x] += 1

for x,y in v.items():
    if y > 0:
        print(x, "=", y)