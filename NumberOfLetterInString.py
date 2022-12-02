# Find the number of occurrences of each letter present in the string!

w = input("Type word: ")
w = w.lower()

letters = {}

for x in w:
    if x in letters:
        letters[x] += 1
    else:
        letters[x] = 1

print(w)

for y,z in letters.items():
    print(f"{y}:{z}")


