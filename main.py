from turtle import *
import time
import turtle
import random
 
screen = Screen()
pendown()
turn = 'x'
 
def start():
 reset()
 user_start = raw_input('Would you like to play Tic Tac Toe? Please type Yes or No: ')
 if user_start == ('Yes') or user_start == ('yes') or user_start == ('Y') or user_start == ('y'):
   print(' Tic - Tac - Toe ')
   print(' The objective of the game is to complete a line of 3 crosses (X)')
   print('   or 3 circles (O) before your opponent.')
   print(' ')
   time.sleep(3)
   uservs()
 elif user_start == ('No') or user_start == ('no') or user_start == ('N') or user_start == ('n'):
   print('Ok. See you next time!')
 else:
   print('Wrong input. Restarting...')
   start()
 
def userokconfirm():
 reset()
 userok = raw_input('User 1 is X. User 2 is O. Please type OK.')
 if userok == ('OK') or userok == ('Ok') or userok == ('ok') or userok == ('K') or userok == ('k'):
   print('Starting Game...')
   setup_game()
 else:
   print('Not a valid input.')
   userokconfirm()
  
def uservs():
 reset()
 user_vs = raw_input('Do want to play User vs. User, User vs. PC, or PC vs. PC? ')
 if user_vs == ('User vs User') or user_vs == ('user vs user'):
   userokconfirm()
 elif user_vs == ('User vs PC') or user_vs == ('user vs pc'):
   userpcconfirm()
 elif user_vs == ('PC vs PC') or user_vs == ('pc vs pc'):
   pcvspc()
 else:
   print('Not acceptable input. Please try again.')
   uservs()
 
def setup_game():
 turtle.penup()
 turtle.speed(0)
 turtle.goto(-200 ,200)
 turtle.forward(100)
 turtle.pendown()
 turtle.right(90)
 turtle.forward(300)
 turtle.penup()
 turtle.right(-90)
 turtle.forward(100)
 turtle.right(-90)
 turtle.pendown()
 turtle.forward(300)
 turtle.penup()
 turtle.goto(-200, 200)
 turtle.right(180)
 turtle.forward(100)
 turtle.right(-90)
 turtle.pendown()
 turtle.forward(300)
 turtle.penup()
 turtle.right(90)
 turtle.forward(100)
 turtle.right(90)
 turtle.pendown()
 turtle.forward(300)
 
def draw_x (location):
 if location == 0:
   turtle.speed(2.5)
   turtle.penup()
   turtle.goto(-175,175)
   turtle.pendown()
   turtle.goto(-125,125)
 
   turtle.penup()
   turtle.goto(-125, 175)
   turtle.pendown()
   turtle.goto(-175, 125)
 
 elif location == 1:
   turtle.speed(2.5)
   turtle.penup()
   turtle.goto(-75,175)
   turtle.pendown()
   turtle.goto(-25,125)
 
   turtle.penup()
   turtle.goto(-25, 175)
   turtle.pendown()
   turtle.goto(-75, 125)
  elif location == 2:
   turtle.speed(2.5)
   turtle.penup()
   turtle.goto( 25,175)
   turtle.pendown()
   turtle.goto( 75,125)
 
   turtle.penup()
   turtle.goto(75, 175)
   turtle.pendown()
   turtle.goto(25, 125)
 
 elif location == 3:
   turtle.speed(2.5)
   turtle.penup()
   turtle.goto(-175, 75 )
   turtle.pendown()
   turtle.goto(-125,25)
 
   turtle.penup()
   turtle.goto(-125, 75)
   turtle.pendown()
   turtle.goto(-175, 25)
 
 elif location == 4:
   turtle.speed(2.5)
   turtle.penup()
   turtle.goto(-75,75)
   turtle.pendown()
   turtle.goto(-25,25)
 
   turtle.penup()
   turtle.goto(-25, 75)
   turtle.pendown()
   turtle.goto(-75, 25)
 
 elif location == 5:
   turtle.speed(2.5)
   turtle.penup()
   turtle.goto(25,75)
   turtle.pendown()
   turtle.goto(75,25)
 
   turtle.penup()
   turtle.goto(75, 75)
   turtle.pendown()
   turtle.goto(25, 25)
 
 elif location == 6:
   turtle.speed(2.5)
   turtle.penup()
   turtle.goto(-175,-25)
   turtle.pendown()
   turtle.goto(-125, -75)
 
   turtle.penup()
   turtle.goto(-125,-25)
   turtle.pendown()
   turtle.goto(-175, -75)
 
 elif location == 7:
   turtle.speed(2.5)
   turtle.penup()
   turtle.goto(-75,-25)
   turtle.pendown()
   turtle.goto(-25,-75)
 
   turtle.penup()
   turtle.goto(-25, -25)
   turtle.pendown()
   turtle.goto(-75, -75)
 
 elif location == 8:
   turtle.speed(2.5)
   turtle.penup()
   turtle.goto(25,-25)
   turtle.pendown()
   turtle.goto(75,-75)
 
   turtle.penup()
   turtle.goto(75, -25)
   turtle.pendown()
   turtle.goto(25, -75)
 
# def draw_o(location):
def draw_o (location):
 if location == 0:
   turtle.speed(2.5)
   turtle.penup()
   turtle.goto(-150, 175)
   turtle.pendown()
   turtle.circle(25)
 
 if location == 1:
   turtle.speed(2.5)
   turtle.penup()
   turtle.goto(-50, 175)
   turtle.pendown()
   turtle.circle(25)
  if location == 2:
   turtle.speed(2.5)
   turtle.penup()
   turtle.goto( 50, 175)
   turtle.pendown()
   turtle.circle(25)
 
 if location == 3:
   turtle.speed(2.5)
   turtle.penup()
   turtle.goto(-150, 75)
   turtle.pendown()
   turtle.circle(25)
  if location == 4:
   turtle.speed(2.5)
   turtle.penup()
   turtle.goto(-50, 75)
   turtle.pendown()
   turtle.circle(25)
  if location == 5:
   turtle.speed(2.5)
   turtle.penup()
   turtle.goto(50, 75)
   turtle.pendown()
   turtle.circle(25)
  if location == 6:
   turtle.speed(2.5)
   turtle.penup()
   turtle.goto(-150 ,-25)
   turtle.pendown()
   turtle.circle(25)
 
 if location == 7:
   turtle.speed(2.5)
   turtle.penup()
   turtle.goto(-50, -25)
   turtle.pendown()
   turtle.circle(25)
 
 if location == 8:
   turtle.speed(2.5)
   turtle.penup()
   turtle.goto(50, -25)
   turtle.pendown()
   turtle.circle(25)
 
def win_check():
   # horizontal check
   for i in range(0, 9, 3):
       if (board[i] == board[i + 1] == board[i + 2]):
           return True
 
   # vertical check
   for i in range(3):
       if (board[i] == board[i + 3] == board[i + 6]):
           return True
 
   # diagonal check
   if ((board[0] == board[4] == board[8]) or (board[2] == board[4] == board[6])):
       return True
 
# user vs user
def play_move (move):
 
 global board, turn, game
 
 if board[move] >= 0 and board[move] <= 8:
   board[move] = turn
   #print ("heres board", board)
 
   if turn == 'o':
     draw_o(move)
     if (win_check()):
       Game_End_Circle()
       game = 'over'
     turn = 'x'
    
   elif turn == 'x':
     draw_x(move)
     if (win_check()):
       Game_End_Cross()
       game = 'over'
     turn = 'o'
 
# user vs computer     
def computer_move (move):
 
 global board, turn, game, random
 
 if board[move] >= 0 and board[move] <= 8:
   board[move] = turn
   #print ("heres board", board)
 
   if turn == 'o':
     move = random.choice(board)
     draw_o(move)
     if (win_check()):
       Game_End_Circle()
       game = 'over'
     turn = 'x'
    
   elif turn == 'x':
     draw_x(move)
     if (win_check()):
       Game_End_Cross()
       game = 'over'
     turn = 'o' 
 
# prints output and ends game if cross wins 
def Game_End_Cross():
 print('----------------------------')
 print('|                          |')
 print('| Congrats! Cross has won! |')
 print('|                          |')
 print('----------------------------')
 time.sleep(2)
 play_again = raw_input('Do you want to play again? ')
 if play_again == ('Yes') or play_again == ('yes') or play_again == ('Y') or play_again == ('y'):
   print('Restarting...')
   time.sleep(1)
   start()
 elif play_again == ('No') or play_again == ('no') or play_again == ('N') or play_again == ('n'):
   print('Ok. See you next time!')
 else:
   print('Not a valid input. Please try again.')
   Game_End_Cross()
  
# prints output and ends game if circle wins
def Game_End_Circle():
 print('-----------------------------')
 print('|                           |')
 print('| Congrats! Circle has won! |')
 print('|                           |')
 print('-----------------------------')
 time.sleep(2)
 play_again = raw_input('Do you want to play again? ')
 if play_again == ('Yes') or play_again == ('yes') or play_again == ('Y') or play_again == ('y'):
   print('Restarting...')
   time.sleep(1)
   start()
 elif play_again == ('No') or play_again == ('no') or play_again == ('N') or play_again == ('n'):
   print('Ok. See you next time!')
 else:
   print('Not a valid input. Please try again.')
   Game_End_Circle()
def which_square (x,y):
 
 """This function will convert the xy coordinate into squares of the tic tac toe board
 [ 0 | 1 | 2 ]
 [ 3 | 4 | 5 ]
 [ 6 | 7 | 8 ]
 """
 
 # # for testing  
 # print ("x and y: ", x, y)
 
 global game
 
 if game == 'over':
   return None
 
 # check which square does the xy coordinate belongs to
 # if not((x < -200) or (x > 100)) or ((y > 200) or (y <-100)):
 if y <= 200 and y >= 100:
   if x >= 0:
     move = 2
   elif x >= -100:
     move = 1
   elif x >= -200:
     move = 0
  elif y < 100 and y >=0:
   if x >= 0:
     move = 5
   elif x >= -100:
     move = 4
   elif x >= -200:
     move = 3
 
 elif y <0 and y >= -100:
   if x >= 0:
     move = 8
   elif x >= -100:
     move = 7
   elif x >= -200:
     move = 6
  # draws
 computer_move(move)
 
# Start Code   
setup_game()
 
game = 'not over'
move = None
board = [0,1,2,3,4,5,6,7,8]
 
# Everytime this function is called, it passes xy coordinate into a function inside the parathensis.
screen.onscreenclick(which_square)
 
# For testing, uncomment to use.
# print("Heres the current board",board)
 
print('User 1, please click where you want to go. (You may have to click twice.)')
 
# screen.mainloop()
