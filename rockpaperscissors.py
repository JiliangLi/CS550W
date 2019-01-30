# Eric Li
# Rock-Paper-Scissors Simulation
# Jan 18, 2019

# the goal of this simulation is to find the best strategy to win the game rock-paper-scissors
# throughout the entire simulation number 1 stands for rock, number 2 stands for paper
# number 3 stands for scissors
# the simulations aims to maximize player1 is winning opportunities
# the rules used in this simulation is identital to that of the actual game

import random
import matplotlib.pyplot as plt

def rules(choice1, choice2):		# function that determines the winner based on the input
	if choice1 == 1 and choice2 == 3:		# rock beats scissors
		return(1)		# 1 means that player1 wins
	elif choice1 - choice2 == 1:		# paper beats rock, scissors beat paper
		return(1)
	elif choice1 == choice2:		# a tie
		return(2)		# 2 suggests a tie
	else:			# what's left: player3 wins
		return(3)		# 3 means that player2 wins

# strategy1,strategy2, and strategy3 are all based on ideal situations where the opponents 
# are assumed to throw gestures randomly

def strategy1():		# first strategy: throw random gestures
	tries = 100
	(player1, player2) = (0,0)
	for x in range(tries):
		player1_choice = random.randrange(1,4)
		player2_choice = random.randrange(1,4)
		result = rules(player1_choice,player2_choice)
		if result == 1:		# if player1 wins
			player1 += 1
		elif result == 3:
			player2 += 1
	
	return player1

def strategy1_plot():		# establish the lists to be plotted
	display1 = [0 for x in range(100)]
	for x in range(100):
		i = strategy1()
		display1[i] += 1
	r1 = [x for x in range(100)]
	return(display1, r1)



def strategy2(x, player1_choice, player2_choice):
	# second strategy: if player1 wins, in the next round he/she will throw the 
	# gesture his/her opponent throws in this round
	global tries, player1, player2
	if x < tries:
		result = rules(player1_choice,player2_choice)
		x += 1
		if result == 1:
			player1 += 1
			strategy2(x, player2_choice, random.randrange(1,4))
		elif result == 2:
			strategy2(x, random.randrange(1,4), random.randrange(1,4))
		else:
			player2 += 1
			strategy2(x, random.randrange(1,4), random.randrange(1,4))

def strategy2_plot():		# establish the lists to be plotted
	global tries, player1, player2
	tries = 100
	display2 = [0 for x in range(100)]
	for x in range(100):
		(player1, player2) = (0,0)
		strategy2(0, random.randrange(1,4), random.randrange(1,4))
		display2[player1] += 1
	r2 = [x for x in range(100)]
	return(display2, r2)



def strategy3(): 	# third strategy, always throw paper
	tries = 100
	(player1, player2) = (0,0)
	for x in range(tries):
		player2_choice = random.randrange(1,4)
		result = rules(2,player2_choice)
		if result == 1:
			player1 += 1
		elif result == 3:
			player2 += 1
	
	return player1

def strategy3_plot():		# establish the lists to be plotted
	display3 = [0 for x in range(100)]
	for x in range(100):
		i = strategy1()
		display3[i] += 1
	r3 = [x for x in range(100)]
	return(display3, r3)

(display1, r1) = strategy1_plot()
(display2, r2) = strategy2_plot()
(display3, r3) = strategy3_plot()

# strategy1_var, strategy2-var, and strategy3_var are all based on more realistic 
# situations where the psychology plays a role in the opponent's decisions
# in particular, extensive reasearches have shown that rock is thrown 35% of the times, 
# paper 35%, and scissor 30%

def strategy1_var(x, player1_choice, player2_choice):	# first strategy: throw random gestures
	global tries, player1, player2

	# creating the differences in the probabilities of each gesture
	idealpool = [1 for x in range(30)] + [2 for x in range(35)] + [3 for x in range(35)]
	expectedpool = [1 for x in range(35)] + [2 for x in range(35)] + [3 for x in range(30)]

	if x < tries:
		result = rules(player1_choice, player2_choice)
		x += 1
		if result == 1:		# if player1 wins
			player1 += 1
			if random.randrange(100) < 55:		
			# creating the 55 chance where the opponent will, in the next round, throw 
			# the gesture that would have given him/her the win in this round
				if player1_choice == 3:
					nextmove = 1
				else:
					nextmove = player1_choice + 1
			else:
				nextmove = random.choice(expectedpool)
			strategy1_var(x, random.choice(idealpool), nextmove)
		else:
			strategy1_var(x, random.choice(idealpool), random.choice(expectedpool))


def strategy1_var_plot():		# establish the lists to be plotted
	global tries, player1, player2
	idealpool = [1 for x in range(30)] + [2 for x in range(35)] + [3 for x in range(35)]
	expectedpool = [1 for x in range(35)] + [2 for x in range(35)] + [3 for x in range(30)]

	tries = 100
	display1 = [0 for x in range(100)]
	for x in range(100):
		(player1, player2) = (0,0)
		strategy1_var(0, random.choice(idealpool), random.choice(expectedpool))	# start recursion
		display1[player1] += 1
	r1 = [x for x in range(100)]
	return(display1, r1)



def strategy2_var(x, player1_choice, player2_choice):
	# second strategy: if player1 wins, in the next round he/she will throw the 
	# gesture his/her opponent throws in this round

	global tries, player1, player2
	
	# creating the differences in the probabilities of each gesture
	idealpool = [1 for x in range(30)] + [2 for x in range(35)] + [3 for x in range(35)]
	expectedpool = [1 for x in range(35)] + [2 for x in range(35)] + [3 for x in range(30)]

	if x < tries:
		result = rules(player1_choice, player2_choice)
		x += 1
		if result == 1:
			player1 += 1
			if random.randrange(100) < 55:
			# creating the 55 chance where the opponent will, in the next round, 
			# throw the gesture that would have given him/her the win in this round
				if player1_choice == 3:
					nextmove = 1
				else:
					nextmove = player1_choice + 1
			else:
				nextmove = random.choice(expectedpool)
			strategy2_var(x, player2_choice, nextmove)
		else:
			strategy2_var(x, random.choice(idealpool), random.choice(expectedpool))

def strategy2_var_plot():		# establish the lists to be plotted
	global tries, player1, player2
	idealpool = [1 for x in range(30)] + [2 for x in range(35)] + [3 for x in range(35)]
	expectedpool = [1 for x in range(35)] + [2 for x in range(35)] + [3 for x in range(30)]

	tries = 100
	display2 = [0 for x in range(100)]
	for x in range(100):
		(player1, player2) = (0,0)
		strategy2_var(0, random.choice(idealpool), random.choice(expectedpool)) # start recursion
		display2[player1] += 1
	r2 = [x for x in range(100)]
	return(display2, r2)


def strategy3_var(x, player1_choice, player2_choice):	# third strategy, always throw paper
	global tries, player1, player2

	# creating the differences in the probabilities of each gesture
	idealpool = [1 for x in range(30)] + [2 for x in range(35)] + [3 for x in range(35)]
	expectedpool = [1 for x in range(35)] + [2 for x in range(35)] + [3 for x in range(30)]

	if x < tries:
		result = rules(player1_choice, player2_choice)
		x += 1
		if result == 1:
			player1 += 1
			if random.randrange(100) < 55:
			# creating the 55 chance where the opponent will, in the next round, 
			# throw the gesture that would have given him/her the win in this round
				if player1_choice == 3:
					nextmove = 1
				else:
					nextmove = player1_choice + 1
			else:
				nextmove = random.choice(expectedpool)
			strategy3_var(x, 2, nextmove)
		else:
			strategy3_var(x, 2, random.choice(expectedpool))

def strategy3_var_plot():		# establish the lists to be plotted
	global tries, player1, player2
	idealpool = [1 for x in range(30)] + [2 for x in range(35)] + [3 for x in range(35)]
	expectedpool = [1 for x in range(35)] + [2 for x in range(35)] + [3 for x in range(30)]

	tries = 100
	display3 = [0 for x in range(100)]
	for x in range(100):
		(player1, player2) = (0,0)
		strategy3_var(0, 2, random.choice(expectedpool))	# start recursion
		display3[player1] += 1
	r3 = [x for x in range(100)]
	return(display3, r3)


(display1_var, r1_var) = strategy1_var_plot()
(display2_var, r2_var) = strategy2_var_plot()
(display3_var, r3_var) = strategy3_var_plot()

plt.plot(r1,display1,'bo', r2, display2,'go', r3, display3,'ro')
plt.ylabel("Number of Appearance")
plt.xlabel("Chances of Winning(%)")
plt.show()

plt.plot(r1_var,display1_var,'bo', r2_var, display2_var,'go', r3_var, display3_var,'ro')
plt.ylabel("Number of Appearance")
plt.xlabel("Chances of Winning(%)")
plt.show()

plt.plot(r1,display1,'bs', r1_var,display1_var, 'ro')
plt.ylabel("Number of Appearance")
plt.xlabel("Chances of Winning(%)")
plt.show()

plt.plot(r2,display2,'bs', r2_var,display2_var, 'ro')
plt.ylabel("Number of Appearance")
plt.xlabel("Chances of Winning(%)")
plt.show()

plt.plot(r3,display3,'bs', r3_var,display3_var, 'ro')
plt.ylabel("Number of Appearance")
plt.xlabel("Chances of Winning(%)")
plt.show()


