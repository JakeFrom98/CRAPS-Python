#Player and “house” start with a score of 0 before the first roll.  Scores for both are accumulated through the number of rolls (1,2, and 3). 
#For each roll of the 2 dice: NOTE – this does not require a loop as we have not covered this, but you may use loops if you have moved ahead and mastered them.
#If the sum of the dice is 7 or 11, display “CRAPS” and increment “house score by 2”.
#If the dice are the same value (doubles) and the values are even, increment the player score by 2 (NOTE – you should use the modulo operator with an operand of 2 for determining whether the value is even). 
#If the dice are the same value (doubles) and the values are odd, increment the “house” score by 2.  
#If not CRAPS or doubles, and the total is less than 7, houseScore = houseScore +2.
#If not CRAPS or doubles, and the total is greater than 7, playerScore = playerScore + 2.
#Determine the winner and display the results (with 3 rolls, there cannot be a tie!).
#Be sure to use comments for both structure of the program and documentation of the code.
#All code must completely be your own individual work product.

import random
d1 = 0
d2 = 0
player = 0
house = 0
numOfRolls = 3
sum = 0
craps = False
d1d2 = d1+d2

print('''
 .----------------.  .----------------.  .----------------.  .----------------.  .----------------. 
| .--------------. || .--------------. || .--------------. || .--------------. || .--------------. |
| |     ______   | || |  _______     | || |      __      | || |   ______     | || |    _______   | |
| |   .' ___  |  | || | |_   __ \    | || |     /  \     | || |  |_   __ \   | || |   /  ___  |  | |
| |  / .'   \_|  | || |   | |__) |   | || |    / /\ \    | || |    | |__) |  | || |  |  (__ \_|  | |
| |  | |         | || |   |  __ /    | || |   / ____ \   | || |    |  ___/   | || |   '.___`-.   | |
| |  \ `.___.'\  | || |  _| |  \ \_  | || | _/ /    \ \_ | || |   _| |_      | || |  |`\____) |  | |
| |   `._____.'  | || | |____| |___| | || ||____|  |____|| || |  |_____|     | || |  |_______.'  | |
| |              | || |              | || |              | || |              | || |              | |
| '--------------' || '--------------' || '--------------' || '--------------' || '--------------' |
 '----------------'  '----------------'  '----------------'  '----------------'  '----------------' 

''')
input('Welcome to CRAPS! Press Enter to roll the dice.')
#For each roll of the 2 dice: NOTE – this does not require 
#a loop as we have not covered this, but you may use loops if 
#you have moved ahead and mastered them.
d1 = random.randint(1,6)
d2 = random.randint(1,6)

#If the sum of the dice is 7 or 11, display “CRAPS” 
#and increment “house score by 2”.
sum = d1 + d2
if sum == 7 or sum == 11:
    print('CRAPS!')
    craps = True
    house = house + 2   #house +=2
   
#If the dice are the same value (doubles) and the values are odd, increment the “house” score by 2.  

if d1 == d2 and (number % 2) == 0:
        #even number
        player = player + 2
       
if d1 == d2 and (number % 2) == 1:
    #odd number 
    house = house + 2   #house +=2

#If not CRAPS or doubles, and the total is less than 7, houseScore = houseScore +2.
for x in range (3):
    if (craps or (d1 == d2)) and sum < 7:
        house = house + 2   #house +=2

#If not CRAPS or doubles, and the total is greater than 7, playerScore = playerScore + 2.
    if (craps or (d1 == d2)) and sum > 7:
        player = player + 2   #player +=2
#Round 1   
#Player       
if (d1 == 1):
    print('''Round 1!
Player
+-----+  
|     |  
|  o  |  
|     |  
+-----+         
''')
    
elif (d1 == 2):
        print('''
Player
+-----+  
|o    |  
|     |  
|    o|  
+-----+     
''')

elif (d1 == 3):
        print('''
Player
+-----+  
|o    |  
|  o  |  
|    o|  
+-----+     
''')

elif (d1 == 4):
        print('''
Player
+-----+  
|o   o|  
|     |  
|o   o|  
+-----+     
''')

elif (d1 == 5):
        print('''
Player
+-----+  
|o   o|  
|  o  |  
|o   o|  
+-----+     
''')

elif (d1 == 6):
        print('''
Player
+-----+  
|o   o|  
|o   o|  
|o   o|  
+-----+     
''')

#House
if (d2 == 1):
    print('''





House
+-----+  
|     |  
|  o  |  
|     |  
+-----+         
''')

elif (d2 == 2):
        print('''
House
+-----+  
|o    |  
|     |  
|    o|  
+-----+     
''')


elif (d2 == 3):
        print('''
House
+-----+  
|o    |  
|  o  |  
|    o|  
+-----+     
''')

elif (d2 == 4):
        print('''
House
+-----+  
|o   o|  
|     |  
|o   o|  
+-----+     
''')

elif (d2 == 5):
        print('''
House
+-----+  
|o   o|  
|  o  |  
|o   o|  
+-----+     
''')

elif (d2 == 6):
        print('''
House
+-----+  
|o   o|  
|o   o|  
|o   o|  
+-----+     
''') 

#Round 2
input('Round 2! Press Enter to roll again')
if (d1 == 1):
    print('''
Player
+-----+  
|     |  
|  o  |  
|     |  
+-----+         
''')
    
elif (d1 == 2):
        print('''
Player
+-----+  
|o    |  
|     |  
|    o|  
+-----+     
''')

elif (d1 == 3):
        print('''
Player
+-----+  
|o    |  
|  o  |  
|    o|  
+-----+     
''')

elif (d1 == 4):
        print('''
Player
+-----+  
|o   o|  
|     |  
|o   o|  
+-----+     
''')

elif (d1 == 5):
        print('''
Player
+-----+  
|o   o|  
|  o  |  
|o   o|  
+-----+     
''')

elif (d1 == 6):
        print('''
Player
+-----+  
|o   o|  
|o   o|  
|o   o|  
+-----+     
''')
#House
if (d2 == 1):
    print('''
House
+-----+  
|     |  
|  o  |  
|     |  
+-----+         
''')

elif (d2 == 2):
        print('''
House
+-----+  
|o    |  
|     |  
|    o|  
+-----+     
''')


elif (d2 == 3):
        print('''
House
+-----+  
|o    |  
|  o  |  
|    o|  
+-----+     
''')

elif (d2 == 4):
        print('''
House
+-----+  
|o   o|  
|     |  
|o   o|  
+-----+     
''')

elif (d2 == 5):
        print('''
House
+-----+  
|o   o|  
|  o  |  
|o   o|  
+-----+     
''')

elif (d2 == 6):
        print('''
House
+-----+  
|o   o|  
|o   o|  
|o   o|  
+-----+     
''') 

#Round 3
input('Round 3! Press Enter to roll again')
if (d1 == 1):
    print('''
Player
+-----+  
|     |  
|  o  |  
|     |  
+-----+         
''')
    
elif (d1 == 2):
        print('''
Player
+-----+  
|o    |  
|     |  
|    o|  
+-----+     
''')

elif (d1 == 3):
        print('''
Player
+-----+  
|o    |  
|  o  |  
|    o|  
+-----+     
''')

elif (d1 == 4):
        print('''
Player
+-----+  
|o   o|  
|     |  
|o   o|  
+-----+     
''')

elif (d1 == 5):
        print('''
Player
+-----+  
|o   o|  
|  o  |  
|o   o|  
+-----+     
''')

elif (d1 == 6):
        print('''
Player
+-----+  
|o   o|  
|o   o|  
|o   o|  
+-----+     
''')

#House
if (d2 == 1):
    print('''
House
+-----+  
|     |  
|  o  |  
|     |  
+-----+         
''')

elif (d2 == 2):
        print('''
House
+-----+  
|o    |  
|     |  
|    o|  
+-----+     
''')


elif (d2 == 3):
        print('''
House
+-----+  
|o    |  
|  o  |  
|    o|  
+-----+     
''')

elif (d2 == 4):
        print('''
House
+-----+  
|o   o|  
|     |  
|o   o|  
+-----+     
''')

elif (d2 == 5):
        print('''
House
+-----+  
|o   o|  
|  o  |  
|o   o|  
+-----+     
''')

elif (d2 == 6):
        print('''
House
+-----+  
|o   o|  
|o   o|  
|o   o|  
+-----+     
''') 
#Who wins?
if (d1 > d2 ):
	print('You Win! Your Score', d1)
	print('House Score', d2) 		
elif (d2 > d1 ): 
	print('House Wins! House Score', d2)
	print('Your Score', d1)