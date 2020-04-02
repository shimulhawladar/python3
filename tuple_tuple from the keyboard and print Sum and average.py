# Write a program to take the tuple from the keyboard and print sum and average'

numbers = input("Type Numbers like 1,2 : " )
numbers = tuple(map(int,numbers.split(',')))
total = 0


for value in numbers:
    total = total + value

avg = total / len(numbers)

print("The Sum of Natural Numbers from 1 to {0} =  {1}".format(numbers, total))
print("Average of Natural Numbers from 1 to {0} =  {1}".format(numbers, avg))
