# partner 1: Oleh Shostak
# partner 2: Eric Li
''' Instructions:
   Work with a partner to complete these tasks. Complete as many as you can. Assume that all variables/lists are declared and initialized (unless you are specifically asked to create/initialize a list); you need only write the code using the variables/lists indicated in the description. Write your solution below the commented description.
'''
 
''' 1. 
   Create a list of ints, faveNums, that holds 3 integers.
'''
faveNums =[x for x in range(3)]
 
 
 
''' 2. 
   Create a list of Strings, holidays, that holds 14 holidays.  
'''
holidays = [14*'holidays']
 
 
''' 3. 
   Create a list of characters, grades, that holds 5 letter grades.
'''
grades = [chr(x) for x in range(65, 70)]
 
 
''' 4. 
   Create a list of booleans, funny, the can keep track of whether 18 things are funny or not. 
'''
 
Funny = True
funny_list = [18*funny]
 
''' 5. 
   Create a list of doubles, salaries, that holds the salaries of all the employees at a university. 
   The number of employees is stored in the int numEmployees.
'''
 
salaries = [0.00 for x in numEmployees]
 
''' 6. 
   A picture's dimensions are stored in integer variables x and y. Create a single list of integers that can store the grayscale value for each pixel in the list.
'''
grayscale_list = y*[[x*[]]]
 
 
''' 7. 
   In a class, each student has 0, 1, 2 or 3 siblings. 
   The numbers of students with no siblings is stored in the variable noSiblings, 
   the number of students with one sibling is stored in the variable oneSibling, 
   the number of students with two siblings is stored in the variable twoSiblings, 
   and the number of students with three siblings is stored in the variable threeSiblings. 
   Create a list that holds all the names of the students in the class, 
   as well as the names of all their siblings.
'''
names = ["name" for x in range(noSiblings + 2*oneSibling + 3*twoSiblings + 4*threeSiblings)]
 
 
 
''' 8. 
   Create a list that holds all the months in the year. (No loop.)
'''
months_list = ['September', 'October', 'November', 'December', 'January', 'February', 'March', 'April', 'May', 'June', 'July', 'August'] 
 
 
''' 9. 
   Create a list that holds all the days of the week. (No loop.)
'''
   week = ["Monday", "Tuesday", "Wednesday", "Thursday",  "Friday", "Saturday", "Sunday"]
 
 
''' 10. 
   Create a list that holds all the possible values for boolean variables. (No loop.)
'''
 
b_list = [True, False] 
 
''' 11. 
   Create a list that holds the names of all the 3rd form dorms on campus. (No loop.)
'''
dorms = ["Memorial", "Nicols", "Pitman", "Squire Stanley"]
 
 
''' 12.  
   Create a list that holds 3 random numbers with values between 0 and 1. (Loop optional.)
'''
import random
a_list = []
for i in range(3):
   a_list.append(random.randint(1))

 
''' 13. 
   Create a list that will represent a deck of cards. Some example data for cards would be AS (ace of spaces), 5H (5 of hearts), JC (jack of clubs), 9D (9 diamonds). (Loop required.) 
'''
deck = []
rank = ['A','2','3','4','5','6','7','8','9','10','J','Q','K']
suit = ['C','H','D','S']
for r in rank:
   for s in suit:
      deck.append(r+s)
   
print(deck)
 
''' 14. 
   Write a Yahtzee program that simulates the rolling of five dice and prints "Yahtzee" if all five dice are the same; otherwise it should print "Try again."
'''
import random
a_list = []
for i in range(6):
   a_list.append(random.randint(0, 7))
for a in range(len(a_list)-2):
   if a_list[a] == a_list[a+1]:
      pass
   else:
      print('Try again!')
      break
print('Yahtzee')
 
 
''' 15. 
   In a list, specials are numbers in a list that have an even number before them, 
   an odd number behind them, and they themselves are divisible by 3. 
   Given a list of ints called numbers, print out the location in the list of the specials, 
   as well as the value in front of them, their value, and the value behind them. For example:
   position 4: 14, 9, 25
'''

numbers = []

for i in range(1,len(numbers)-1):
   if numbers[i-1] % 2 == 0 and numbers[i] % 3 == 0 and numbers[i+1] % 2 == 1:
      print("position " + str(i) + ": " + str(numbers[i-1]) + ", " + str(numbers[i]) + ", " + str(numbers[i+1]))

 
 
 
''' 16. 
   Write a program to search for the "saddle points" in a 5 by 5 list of integers. 
   A saddle point is a cell whose value is greater than or equal to any in its row, and less than or equal to any in its column. 
   There may be more than one saddle point in the list. 
   Print out the coordinates of any saddle points your program finds. 
   Print out "No saddle points" if there are none.
'''

thelist = [[10,12,7,3,12],[3,10,6,2,8],[18,24,17,16,10],[15,21,10,8,12],[1,18,22,4,15]]
saddle = []

for x in range(5):

   coordinate1 = []
   coordinate2 = []

   biggest = [x,0]

   for y in range(1,5):
      if thelist[x][y] >= thelist[biggest[0]][biggest[1]]:
         biggest = [x,y]
   coordinate1.append(biggest)

   for y in range(len(coordinate1)):
      smallest = [0,coordinate1[y][1]]
      for i in range(1,5):
         if thelist[i][coordinate1[y][1]] <= thelist[smallest[0]][smallest[1]]:
            smallest = [i,coordinate1[y][1]]
      
      coordinate2.append(smallest)

   for y in range(len(coordinate2)):
      if coordinate2[y] in coordinate1:
         saddle.append(coordinate2[y])


if len(saddle) > 0:
   print(saddle)
else:
   print("No saddle points")


''' 17. 
   In the game of chess, a queen can attack pieces which are on the same row, column, or diagonal. 
   A chessboard can be represented by an 8 by 8 list. 
   A 1 in the list represents a queen on the corresponding square, 
   and a O in the list represents an unoccupied square. 
   Given the two locations for queens (row1, col1, row2, col2), 
   place the queens in the 2D list, chessboard. 
   Then process the board and indicate whether or not the two queens are positioned 
   so that they attack each other. 
'''
chessboard = [[0 for x in range(8)] for y in range(8)]

row1 = 1
row2 = 3
col1 = 2
col2 = 4
chessboard[row2-1][col2-1] = 1

attack = False

for x in range(8):
   if chessboard[row1-1][x] == 2:
   if chessboard[row1-1][x] == 1 or chessboard[x][col1-1] == 1:
      attack = True

for x in range(8):
   if row1-1+x < 8 and col1-1+x < 8:
      if chessboard[row1-1+x][col1-1+x] == 1:
         attack = True 
   if row1-1-x >= 0 and col1-1-x >= 0:
      if chessboard[row1-1-x][col1-1-x] == 1:
         attack = True

chessboard[row1-1][col1-1] = 1

for x in range(8):
   print(*chessboard[x])

print(attack)


 
''' 18. 
   Given a list, write code that will reverse the order of the elements in the list. For example, dog, cat, bunny should become bunny, cat, dog.
'''
 
 a_list.reverse()
 
 
''' 19. 
   Given a list, doorknobs, that holds strings, swap the elements at positions 1 and 3, if possible.
'''

if len(doorknobs) >= 4:
   doorknobs[1], doorknobs[3] = doorknobs[3], doorknobs[1]
 
 
''' 20. 
   In a list of ints called numbers, find the largest number in the list and place it at the end of the list.
'''

a_list.sort()


''' 21. 
   In a 2D list with dimensions w by h, filled with random numbers from from 1 to 100, 
   replace every odd number with either 2 or 22; 2 if the number was a single digit number, 
   22 if the number was a 2-digit number. 
'''

import random as r


thelist = [[r.randrange(1,101) for x in range(w)]for y in range(h)]

for x in range(w):
   for y in range(h):
      if thelist[x][y] % 2 == 1:
         if len(str(thelist[x][y])) == 1:
            thelist[x][y] = 2
         else:
            thelist[x][y] = 22

print(thelist)
 
 
''' 22. 
   In a 2D list with dimensions w by h, holding grayscale values for an image, adjust the colors so the image is inverted. All light portions should be dark, all dark portions should be light. A value of 200 should be 5, a value of 100 should be 155, etc. Remember, there are 256 levels for color, including 0.
'''

a_list = [w*[h*[]]]
for w in range(w-1):
   for h in range(h-1):
      a_list[w][h] = 255 - a_list[w][h]
 
 
''' 23.
   In a list, shifters, holding ints, shift all elements forward 1 position. 
   For example, position 2 should move to position 1, position 1 to position 0, 
   and position 0 to the end of the list (etc.)
'''
shifters = [0,1,2,3,4,5]
position0 = shifters[0]
shifters.pop(0)
shifters.append(position0)
 
''' 24. 
   Given an N-by-N grid of elevation values (in meters), a peak is a grid point for which all four neighboring cells are strictly lower. Write a code fragment that counts the number of peaks in a given N-by-N grid.
'''

game_board = [(n+2)*[] for i in range(n+2)]
peaks_number = 0

for a in range(len(game_board)-1):
   for i in range(len(game_board[i])-1):
      if game_board[a][i+1] < game_board[a][i] :
         if game_board[a][i-1] < game_board[a][i] :
            if game_board[a-1][i] < game_board[a][i] :
               if game_board[a+1][i] < game_board[a][i] :
                  if game_board[a+1][i-1] < game_board[a][i] :
                     if game_board[a-1][i-1] < game_board[a][i] :
                        if game_board[a+1][i+1] < game_board[a][i] :
                           if game_board[a-1][i+1] < game_board[a][i] :
                              peaks_number +=1
  
 
''' 25. 
   90% of incoming college students rate themselves as above average. 
   Write some code that, given a list of student rankings (stored in integer list rankings), 
   prints the fraction of values that are strictly above the average value.
'''

average = 0
for x in range(len(rankings)):
   average += rankings[x]

average = average / len(rankings)

above_average = []

for x in range(len(rankings)):
   if rankings[x] > average:
      above_average.append(rankings[x])

print(above_average)
 
''' 26. 
   Given a 9-by-9 list of integers between 1 and 9, check if it is a valid solution to a Sudoku puzzle: 
   each row, column, and block should contain the 9 integers exactly once.
'''
# sudoku = [[2,3,7,6,9,1,5,8,4],[8,1,5,3,7,4,9,2,6],[6,4,9,2,5,8,3,7,1],[9,8,2,5,6,7,1,4,3],[5,6,3,4,1,2,7,9,8],[4,7,1,8,3,9,2,6,5],[7,9,6,1,4,3,8,5,2],[3,5,8,7,2,6,4,9,],[1,2,4,9,8,5,6,3,7]]

valid = True
for x in range(9):
   for i in range(1,10):
      row_count = 0
      col_count = 0
      for y in range(9):
         if sudoku[x][y] == i:
            row_count += 1
         if sudoku[y][x] == i:
            col_count += 1
      if row_count > 1 or col_count > 1:
         valid = False

for x in range(1,8,3):
   for y in range(1,8,3):
      for k in range(1,10):
         count = 0
         for i in range(-1,2):
            for j in range(-1,2):
               if sudoku[x+i][y+j] == k:
                  count += 1
         if count > 1: 
            valid = False

for x in range(9):
   print(*sudoku[x])


print(valid)

 
'''
    27. Create a list of 100 numbers between 1 and 10 (inclusive), 
    create a new list whose first value is the number of 1s in the original list, 
    whose 2nd value is the number of 2s in the original list, and so on. 
    Average the number of occurences of each number in the list over 100 repetitions. 
    Average the averages. Print the result to the screen.
'''
import random as r

newnewlist= []

for i in range(100):  
   numbers = [r.randrange(1,11) for x in range(100)]
   newlist = []
   for y in range(1,11): 
      count = 0 
      for x in range(100):
         if numbers[x] == y:
            count += 1
      newlist.append(count)
   newnewlist.append(newlist)

finallist= []
for x in range(10):
   average = 0
   for y in range(100):
      average += newnewlist[y][x]
   average = average/100
   finallist.append(average)

average = 0
for x in range(10):
   average += finallist[x]

average = average/10

print("The average number of occurence of each number is: " + str(average))

 
 
 
''' Sources
   http://users.csc.calpoly.edu/~jdalbey/103/Projects/ProgrammingPractice.html
   http://introcs.cs.princeton.edu/java/14array/
'''