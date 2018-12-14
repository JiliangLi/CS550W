# Partner 1: Justin Lin
# Partner 2: Eric Li
''' 1.
	Variable grade is a character. If it is an A, print good work. 
'''

if grade.upper() == "A":
   print("Good work.")

''' 2.
   Variable yards is an int. If it is less than 17, multiply yards by 2. 
'''
if years < 17:
   print(years*2)
  
''' 3. 
   Variable success is a boolean. If something is a success, print congratulations. 
'''
if success == True:
   print("congratulations")
 
 
''' 4. 
   Variable word is a String. If the string's second letter is 'f', print fun. 
'''
if word[1].lower() == 'f':
   print('fun')
 
''' 5. 
   Variable temp is a float. Variable celsius is a boolean. If celsius is true, convert to fahrenheit, storing the result in temp. F = 1.8C + 32.
'''
if celsius == True:
   F = 1.8*C + 32
 
 
''' 6. 
   Variable numItems is an int. Variable averageCost and totalCost are floats. If there are items, calculate the average cost. If there are no items, print no items.
'''
if numItems > 0:
   averageCot = totalCost/numItems
   print(averageCost)
else:
   print("No items")
 
''' 7. 
   Variable pollution is a float. Variable cutoff is a float. If pollution is less than the cutoff, print safe condition. If pollution is greater than or equal to cutoff, print unsafe condition. 
'''
 
if pollution < cutoff:
   print("safe condition")
elif pollution >=cutoff:
   print("unsafe condition")


''' 8. 
   Variable score is a float, and grade is a character. Store the appropriate letter grade based on score in the grade variable according to this chart.
   F: <60; B: 80-89; D: 60-69; A: 90-100; C: 70-79.
'''
 
if score < 60:
   grade = "F"
elif score <= 69:
   grade = "D"
elif score <= 79:
   grade = "C"
elif score <= 89:
   grade = "B"
else:
   grade = "A"

''' 9. 
   Variable letter is a character. If it is a lowercase letter, print lowercase. If it is an uppercase, print uppercase. If it is 0-9, print digit. If it is none of these, print symbol.
'''
if 97 <= ord(letter) <= 122:
  print("lowercase")
elif 65 <= ord(letter) <= 90:
   print("uppercase")
elif 49 <= ord(letter) <= 57:
   print("digit")
else:
   print("symbol")
 
 
''' 10. 
   Variable neighbors is an int. Determine where you live based on your neighbors.
   50+: city; 25+: suburbia; 1+: rural; 0: middle of nowhere. 
'''
 
if neighbors > 50:
   print("you live in a city")
elif neighbors > 25:
   print("you live in a suburbian area")
elif neighbors > 1:
   print("you live in a rural area")
else:
   print("you live in the middle of nowhere")
 
''' 11. 
   Variables doesSignificantWork, makesBreakthrough, and nobelPrizeCandidate are booleans. A nobel prize winner does significant work and makes a break through. Store true in nobelPrizeCandidate if they merit the award and false if they don't. 
'''
 
if doesSignificantWork == True and makesBreakthrough == True:
   nobelPrizeCandidate = True
else:
   nobelPrizeCandidate = False

 
''' 12. 
   Variable tax is a boolean, price and taxRate are floats. If there is tax, update price to reflect the tax you must pay.
'''
 
if tax == True:
   price = price*(1+taxRate)
 
''' 13.  
   Variable word and type are Strings. Determine (not super accurately) what kind of word it is by looking at how it ends. 
   -ly: adverb; -ing; gerund; -s: plural; something else: error   
'''
 
if word[-2:] == "ly":
   types = "adverb" 
elif word[-3:] == "ing":
   types = "gerund"
elif word[-1] == "s":
   types = "plural"
else:
   types = "error"
 
''' 14. 
   If integer variable currentNumber is odd, change its value so that it is now 3 times currentNumber plus 1, otherwise change its value so that it is now half of currentNumber (rounded down when currentNumber is odd). 
'''
if currenNumber%2 != 0:
   currentNumber = 3*currentNumber + 1
else:
   currentNumber = currentNumber//2

 
''' 15. 
   Assign true to the boolean variable leapYear if the integer variable year is a leap year. (A leap year is a multiple of 4, and if it is a multiple of 100, it must also be a multiple of 400.) a 
'''

if year%4 == 0 or (year%100 == 0 and year%400 == 0):
   leapYear = True
else:
   leapYear = False
 
''' 16. 
   Determine the smallest of three ints, a, b and c. Store the smallest one of the three in int result. 
'''

if a >= b:
   if c >= b:
      smallestNum = b
   else:
      smallestNum = c

else: 
   if c <= a:
      smallestNum = c
   else:
      smallestNum = a


''' 17. 
   If an int, number, is even, a muliple of 5, and in the range of -100 to 100, then it is a special number. Store whether a number is special or not in the boolean variable special. 
'''
 
if number%2 == 0 and number%5 == 0 and -100 <= number <= 100:
   special = True
else:
   special = False
 
''' 18. 
   Variable letter is a char. Determine if the character is a vowel or not by storing a letter code in the int variable code.
   a/e/o/u/i: 1; y: -1; everything else: 0
'''
 
vowel = ["a", "e", "o", "u", "i"]

if letter.lower() in vowel:
   code = 1
elif letter.lower() == "y":
   code = -1
else:
   code = 0
 
''' 19. 
   Given a string dayOfWeek, determine if it is the weekend. Store the result in boolean isWeekend.
'''
   if dayOfWeek.lower() == "saturday" or dayOfWeek.lower() == "sunday":
      isWeekend = True
   else:
      isWeekend = False
''' 20. 
   Given a String variable month, store the number of days in the given month in integer variable numDays. 
'''
if month == "Jan." or "Mar." or "May" or "Jul." or "Aug." or "Oct." or "Dec.":
   numDays = 31
elif month == "Feb.":
   numDays = 28
else:
   numDays = 30
 
 
''' 21. 
   Three integers, angle1, angle2, and angle3, supposedly made a triangle. Store whether the three given angles make a valid triangle in boolean variable validTriangle.
'''
if angle1 + angle2 + angle3 == 180 and angle1 > 0 and angle2 > 0 and angle3 > 0:
   validTriangle = True
 
 
''' 22. 
   Given an integer, electricity, determine someone's monthly electric bill, float payment, following the rubric below. 
   First 50 units: 50 cents/unit
   Next 100 units: 75 cents/unit
   Next 100 units: 1.20/unit
   For units above 250: 1.50/unit, plus an additional 20% surcharge.
'''
 
if electricity <= 50:
   payment = 50*electricity
elif electricity <= 150:
   payment = 50*50 + 75*(electricity-50)
elif electricity <= 250:
   payment = 50*50 + 75*100 + 120*(electricity-150)
elif electricity >= 250:
   payment = 50*50 + 75*100 + 120*100 + 150*(electricity-250)*1.2
 
''' 23.
   String, greeting, stores a greeting. String language stores the language. If the language is English, greeting is Hello. If the language is French, the greeting is Bonjour. If the language is Spanish, the greeting is Hola. If the language is something else, the greeting is something of your choice.
'''

if language == "English":
   greeting = "Hello"
elif language == "French":
   greeting = "Bonjour"
elif language == "Spanish":
   greeting = "Hola"
else:
   greeting = "~!@#$%^&*"


 
''' 24. 
   Generate a phrase and store it in String phrase, given an int number and a String noun. Here are some sample phrases:
   number: 5; noun: dog; phrase: 5 dogs
   number: 1; noun: cat; phrase: 1 cat
   number: 0; noun: elephant; phrase: 0 elephants
   number: 3; noun: human; phrase: 3 humans
   number: 1; noun: home; phrase: 3 homes
'''
   phrase = str(number) + " " + noun
  
 
''' 25. 
   If a string, userInput, is bacon, print out, "Why did you type bacon?". If it is not bacon, print out, "I like bacon." 
'''
userInput = input("What's your favorite food?")

if userInput == "bacon":
   print("Why did you type bacon?")

else:
   print("I like bacon.")
 
''' 26.
   Come up with your own creative tasks someone could complete to practice if-statements. Also provide solutions.
'''
 
''' Task 1:
   Given an integer Number, determine if its last digit is 7. Store the result in boolean isSeven
'''
# solution
if str(Number)[-1] == "7":
   isSeven = True
else:
   isSeven = False
   
''' Task 2:
   Variable Length is the measurement of a distance in meters. If boolean needConversion indicates that the unit needs to be converted to feet, convert it to feet.
   Round the answer to its closest whole number
   Then build another variable LengthInInches that stores the measurement in inches
   Print out the answers, both in feet and inches, in one sentence
'''

# solution
if needConversion == True:
   Length = round(3.28084*Length)
   LengthInInches = 12*Length
   print("The measurement is " + str(Length) + " in feet and " + str(LengthInInches) + "in inches.")

 
 
''' Task 3:
write a program that will select the largest number in a list of positive numbers. Please use 1 or more if statements. 
'''
 
# solution
def maxnum(nums):
   a = 0
       for x in nums:
           if a < x:
               a = x
       return a

 
''' Sources
 http://www.bowdoin.edu/~ltoma/teaching/cs107/spring05/Lectures/allif.pdf
 http://www.codeforwin.in/2015/05/if-else-programming-practice.html
 Ben Dreier for pointing out some creative boolean solutions.
'''