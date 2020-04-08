#w = input("TypeWords: ")
dic = {
    "Name"      : "Shimul",
    "Subject"   : "Python",
    "Topic"     : "Dictionary"
}
# Output
print(dic,"\n")

# Check the length
print(len(dic),"\n")

# Print Key And Values
for key,val in dic.items():
    print (key, "=>", val)

# Add Value to the directory
dic["year"] = 2020
print("\n",dic)

# Remove a Key and it's Value
del dic["year"]
print("\n",dic,"\n")

# Test the dictionary
print("Name" in dic)
print("name" in dic)

for k in dic:
    if "Name" in k:
        print("Key Found")
        break
    else:
        print("No Key Found")


# Get a value of a specified key
g = dic.get("Name")
print("\n",g)

# Get all keys from the dictionary
ks = dic.keys()
print("\n",ks)
for k in ks:
    print(k)

print("\n")

# Printing the values
for k in dic:
    value = dic[k]
    print(value)



