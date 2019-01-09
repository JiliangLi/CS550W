import random

total_numbers = [0 for x in range(11)]

for x in range(100000):
	number = 0
	for y in range(10):
		n = random.randrange(2)
		if n == 0:
			number += 1
	total_numbers[number] += 1

print(total_numbers)


#print("...", end= "")