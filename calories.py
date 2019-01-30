import random


count = [0 for x in range(9*500*30)]

for x in range(1000):
	parties = random.randrange(0,9)
	servings = random.randrange(1,31)
	for x in range(servings):
		
	calories = random.randrange(50,501)
	total_cal = paries*calories*servings
	count[total_cal] += 1

a
