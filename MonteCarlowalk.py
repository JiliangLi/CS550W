# What is the longest walk you can take where you'll be within walking distance of home at least 50% of the time?
# answer: 22




# What are Monte Carlo simulations? What can they be used for? How do they work? 
# Monte Carlo simulations are simulations that use patterns found in a large collection of random samples to help solve complex problems.
# They do so by revealing the behaviors of complex systems, which are hard to be modeled through exhaustive numerical evaluations.
# Because of this we are able to see the likelihood of each result, and then analyze the results through optimizing their likelihoods.
# They are useful in science, for instance they can be used to model the random motion of particles.
# They can be used to predict business trends and perform risk analysis.
# They can also be applied to problems in finance, engineering, and so on.
# They can even be used to model our daily schedules and life patterns.
# They work by calculating the possible results through a set algorithm.
# The algorithm takes a range of values that has inherent uncertainty as its range of input. 
# It then calculates results over and over, each the choosing its input from the given range randomly.
# Over time a pattern can be seen through a collection of random results. 
# Through the pattern the behavior of the system is shown and the results can be optimzied.
import random

def randomwalk(number):
	(x,y) = (0,0)
	for i in range(number):
		(dx,dy) = random.choice([(0,1),(1,0),(-1,0),(0,-1)])
		x += dx
		y += dy
	return abs(x)+abs(y)

xs = []
for i in range(10):
	for x in range(25):
		walk = x
		trials = 1000
		walkhome = 0
		for j in range(trials):
			if randomwalk(walk) <= 4:
				walkhome += 1
		if 100*(walkhome/trials) > 50:
			xs.append(x)

xs.sort(reverse=True)

print(xs[0])



import random


tries = 10000

count = 0
for x in range(tries):
	(x,y) = (0,0)
	x += random.randrange(-1000,1001)/1000
	y += random.randrange(-1000,1001)/1000
	if (x**2+y**2)**0.5 <= 1:
		count += 1

print(count*4/tries)

# with 100 tries: 3.48 
# with 1000 tries: 3.168 
# with 10,000 tries: 3.1316 
# with 100,000 tries: 3.14162
# the output gets closer to pi





