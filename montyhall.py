# eric li monty hall simulation
# Jan 8, 2019

# it would be better to switch because the chance of having the key behind the other two doors is 2/3.
# in other words the chance of having the key behind my door is 1/3
# when a door holding pennies gets revealed, the chance of having the key behind my door is still 1/3
# so even though now there's only two doors left, the chance is not 50-50
# rather, it should be 1/3 behind my door, and 2/3 behind the other door




# simulation where I don't switch my choice
import random

number = 0
# the revealing part doesn't affect the result because I don't switch my choice afterwards
for x in range(1000):
	doors = [0,0,0]
	key = random.randrange(3)
	doors[key] = 1
	choice = random.randrange(3)
	if choice == key:
		number += 1
print(number)




# simulation where I switch my choice
import random

number = 0

for x in range(1000):
	doors = [0,0,0]
	key = random.randrange(3)
	doors[key] = 1
	choice = random.randrange(3)

	# if my door holds the key and I switch, I get nothing
	if choice == key:
		pass
	# if my door does not hold the key and the other door holding pennies is revealed, I get the key when I switch my choice to the door that is not revealed
	else:
		number += 1

print(number)


# when I don't switch my choice, I won 338 times, about 1/3 of 1000
# when I switch my choice, I won 671 times, about 2/3 of 1000
# this is what I expected
# this happens because mathematically speaking revealing the door and switching my choice are not independent events
# in other words, when the host reveals the door he/she do not reveal it randomly
# because although it is true that the host can reveal either of the two doors when the contestant chooses the door holding the key
# the host is only able to reveal one of the two doors (the only one that does not hold the key) when the contestant chooses the door holding pennies
# (the door to be revaeled is dependent upon the door the contestant picks)
# thus this is different from choosing randomly between two options
# it is more like choosing among three options when a hint favoring the contestant is given
# thus the reasoning given at top holds true
