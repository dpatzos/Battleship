# Patzonidis Dimitrios , A.M.: 4471

import random
from string import *

board = []

ships_p1=[]
ships_p2=[]
ultra_board1=[]
ultra_board2=[]
def board(ultra_board):
    stili=[" ","1","2","3","4","5"]
    ultra_board.append(stili)
    stili=["a"," "," "," "," "," "]
    ultra_board.append(stili)
    stili=["b"," "," "," "," "," "]
    ultra_board.append(stili)
    stili=["c"," "," "," "," "," "]
    ultra_board.append(stili)
    stili=["d"," "," "," "," "," "]
    ultra_board.append(stili)
    stili=["e"," "," "," "," "," "]
    ultra_board.append(stili)
    return ultra_board
board(ultra_board1)
board(ultra_board2)
print ("   P1","             P2")
for i in  range(len(ultra_board1)):
    print ("".join(ultra_board1[i] ),"        ","".join(ultra_board2[i]))
print ("Let's play Battleship!")

no_of_players=input("Input 1 for 1-player game or 2 for 2-player game: ")
while no_of_players!="1" and no_of_players!="2":
    no_of_players=input("Invalid number, please input 1 for 1-player game or 2 for 2-player game: ")
if no_of_players=="2":

    hit_counter_p1=0
    hit_counter_p2=0
    
    all_ships_p1=[]
    all_ships_p2=[]
    ena_ews_pente=["1","2","3","4","5"]
    a_ews_e=["a","b","c","d","e"]
    ship_1_p1=input("Player 1 enter the position of your ship no. 1: ")
    while len(ship_1_p1)!=2:
        ship_1_p1=input("Invalid position. Try again: ")

    ship_col_1_p1=ship_1_p1[1]
    Ship_row_1_p1=ship_1_p1[0]
    while (Ship_row_1_p1 not in a_ews_e) or (ship_col_1_p1 not in ena_ews_pente) :
        ship_1_p1=input("Invalid position. Try again: ")
        ship_col_1_p1=ship_1_p1[1]
        Ship_row_1_p1=ship_1_p1[0]

    Ship_row_1_p1 = Ship_row_1_p1.lower()
    ship_row_1_p1 = []
    for character in Ship_row_1_p1:
        number = ord(character) - 96
        ship_row_1_p1.append(number)
        ship_row_1_p1=ship_row_1_p1[0]
    ship_row_1_p1=int(ship_row_1_p1)
    ship_col_1_p1=int(ship_col_1_p1)
    all_ships_p1.append(ship_1_p1)

    ship_2_p1=input("Player 1 enter the position of your ship no. 2: ")
    while len(ship_2_p1)!=2:
        ship_2_p1=input("Invalid position. Try again: ")

    ship_col_2_p1=ship_2_p1[1]
    Ship_row_2_p1=ship_2_p1[0]
    while (Ship_row_2_p1 not in a_ews_e) or (ship_col_2_p1 not in ena_ews_pente) or (ship_2_p1 in all_ships_p1):
        ship_2_p1=input("Invalid position, or position already taken. Try again: ")
        ship_col_2_p1=ship_2_p1[1]
        Ship_row_2_p1=ship_2_p1[0]

    Ship_row_2_p1 = Ship_row_2_p1.lower()
    ship_row_2_p1 = []
    for character in Ship_row_2_p1:
        number = ord(character) - 96
        ship_row_2_p1.append(number)
        ship_row_2_p1=ship_row_2_p1[0]
        ship_col_1_p1=ship_2_p1[1]
    ship_row_2_p1=int(ship_row_2_p1)
    ship_col_2_p1=int(ship_col_2_p1)
    all_ships_p1.append(ship_2_p1)

    ship_3_p1=input("Player 1 enter the position of your ship no. 3: ")
    while len(ship_3_p1)!=2:
        ship_3_p1=input("Invalid position. Try again: ")

    ship_col_3_p1=ship_3_p1[1]
    Ship_row_3_p1=ship_3_p1[0]
    while (Ship_row_3_p1 not in a_ews_e) or (ship_col_3_p1 not in ena_ews_pente) or (ship_3_p1 in all_ships_p1):
        ship_3_p1=input("Invalid position, or position already taken. Try again: ")
        ship_col_3_p1=ship_3_p1[1]
        Ship_row_3_p1=ship_3_p1[0]

    Ship_row_3_p1 = Ship_row_3_p1.lower()
    ship_row_3_p1 = []
    for character in Ship_row_3_p1:
        number = ord(character) - 96
        ship_row_3_p1.append(number)
        ship_row_3_p1=ship_row_3_p1[0]
        ship_col_3_p1=ship_3_p1[1]
    ship_row_3_p1=int(ship_row_3_p1)
    ship_col_3_p1=int(ship_col_3_p1)
    all_ships_p1.append(ship_3_p1)

    ship_4_p1=input("Player 1 enter the position of your ship no. 4: ")
    while len(ship_4_p1)!=2:
        ship_4_p1=input("Invalid position. Try again: ")

    ship_col_4_p1=ship_4_p1[1]
    Ship_row_4_p1=ship_4_p1[0]
    while (Ship_row_4_p1 not in a_ews_e) or (ship_col_4_p1 not in ena_ews_pente) or (ship_4_p1 in all_ships_p1):
        ship_4_p1=input("Invalid position, or position already taken. Try again: ")
        ship_col_4_p1=ship_4_p1[1]
        Ship_row_4_p1=ship_4_p1[0]

    Ship_row_4_p1 = Ship_row_4_p1.lower()
    ship_row_4_p1 = []
    for character in Ship_row_4_p1:
        number = ord(character) - 96
        ship_row_4_p1.append(number)
        ship_row_4_p1=ship_row_4_p1[0]
    ship_row_4_p1=int(ship_row_4_p1)
    ship_col_4_p1=int(ship_col_4_p1)
    all_ships_p1.append(ship_4_p1)

    ship_5_p1=input("Player 1 enter the position of your ship no. 5: ")
    while len(ship_5_p1)!=2:
        ship_5_p1=input("Invalid position. Try again: ")

    ship_col_5_p1=ship_5_p1[1]
    Ship_row_5_p1=ship_5_p1[0]
    while (Ship_row_5_p1 not in a_ews_e) or (ship_col_5_p1 not in ena_ews_pente) or (ship_5_p1 in all_ships_p1):
        ship_5_p1=input("Invalid position, or position already taken. Try again: ")
        ship_col_5_p1=ship_5_p1[1]
        Ship_row_5_p1=ship_5_p1[0]

    Ship_row_5_p1 = Ship_row_5_p1.lower()
    ship_row_5_p1 = []
    for character in Ship_row_5_p1:
        number = ord(character) - 96
        ship_row_5_p1.append(number)
        ship_row_5_p1=ship_row_5_p1[0]
    ship_row_5_p1=int(ship_row_5_p1)
    ship_col_5_p1=int(ship_col_5_p1)
    all_ships_p1.append(ship_5_p1)

    ship_1_p2=input("Player 2 enter the position of your ship no. 1: ")
    while len(ship_1_p2)!=2:
        ship_1_p2=input("Invalid position. Try again: ")

    ship_col_1_p2=ship_1_p2[1]
    Ship_row_1_p2=ship_1_p2[0]
    while (Ship_row_1_p2 not in a_ews_e) or (ship_col_1_p2 not in ena_ews_pente):
        ship_1_p2=input("Invalid position. Try again: ")
        ship_col_1_p2=ship_1_p2[1]
        Ship_row_1_p2=ship_1_p2[0]

    Ship_row_1_p2 = Ship_row_1_p2.lower()
    ship_row_1_p2 = []
    for character in Ship_row_1_p2:
        number = ord(character) - 96
        ship_row_1_p2.append(number)
        ship_row_1_p2=ship_row_1_p2[0]
    ship_row_1_p2=int(ship_row_1_p2)
    ship_col_1_p2=int(ship_col_1_p2)
    all_ships_p2.append(ship_1_p2)

    ship_2_p2=input("Player 2 enter the position of your ship no. 2: ")
    while len(ship_2_p2)!=2:
        ship_2_p2=input("Invalid position. Try again: ")

    ship_col_2_p2=ship_2_p2[1]
    Ship_row_2_p2=ship_2_p2[0]
    while (Ship_row_2_p2 not in a_ews_e) or (ship_col_2_p2 not in ena_ews_pente) or (ship_2_p2 in all_ships_p2):
        ship_2_p2=input("Invalid position, or position already taken. Try again: ")
        ship_col_2_p2=ship_2_p2[1]
        Ship_row_2_p2=ship_2_p2[0]

    Ship_row_2_p2 = Ship_row_2_p2.lower()
    ship_row_2_p2 = []
    for character in Ship_row_2_p2:
        number = ord(character) - 96
        ship_row_2_p2.append(number)
        ship_row_2_p2=ship_row_2_p2[0]
        ship_col_1_p2=ship_2_p2[1]
    ship_row_2_p2=int(ship_row_2_p2)
    ship_col_2_p2=int(ship_col_2_p2)
    all_ships_p2.append(ship_2_p2)

    ship_3_p2=input("Player 2 enter the position of your ship no. 3: ")
    while len(ship_3_p2)!=2:
        ship_3_p2=input("Invalid position. Try again: ")

    ship_col_3_p2=ship_3_p2[1]
    Ship_row_3_p2=ship_3_p2[0]
    while (Ship_row_3_p2 not in a_ews_e) or (ship_col_3_p2 not in ena_ews_pente) or (ship_3_p2 in all_ships_p2):
        ship_3_p2=input("Invalid position, or position already taken. Try again: ")
        ship_col_3_p2=ship_3_p2[1]
        Ship_row_3_p2=ship_3_p2[0]

    Ship_row_3_p2 = Ship_row_3_p2.lower()
    ship_row_3_p2 = [] 
    for character in Ship_row_3_p2:
        number = ord(character) - 96
        ship_row_3_p2.append(number)
        ship_row_3_p2=ship_row_3_p2[0]
        ship_col_3_p2=ship_3_p2[1]
    ship_row_3_p2=int(ship_row_3_p2)
    ship_col_3_p2=int(ship_col_3_p2)
    all_ships_p2.append(ship_3_p2)

    ship_4_p2=input("Player 2 enter the position of your ship no. 4: ")
    while len(ship_4_p2)!=2:
        ship_4_p2=input("Invalid position. Try again: ")

    ship_col_4_p2=ship_4_p2[1]
    Ship_row_4_p2=ship_4_p2[0]
    while (Ship_row_4_p2 not in a_ews_e) or (ship_col_4_p2 not in ena_ews_pente) or (ship_4_p2 in all_ships_p2):
        ship_4_p2=input("Invalid position, or position already taken. Try again: ")
        ship_col_4_p2=ship_4_p2[1]
        Ship_row_4_p2=ship_4_p2[0]
    Ship_row_4_p2 = Ship_row_4_p2.lower()
    ship_row_4_p2 = []
    for character in Ship_row_4_p2:
        number = ord(character) - 96
        ship_row_4_p2.append(number)
        ship_row_4_p2=ship_row_4_p2[0]
    ship_row_4_p2=int(ship_row_4_p2)
    ship_col_4_p2=int(ship_col_4_p2)
    all_ships_p2.append(ship_4_p2)

    ship_5_p2=input("Player 2 enter the position of your ship no. 5: ")
    while len(ship_5_p2)!=2:
        ship_5_p2=input("Invalid position. Try again: ")

    ship_col_5_p2=ship_5_p2[1]
    Ship_row_5_p2=ship_5_p2[0]
    while (Ship_row_5_p2 not in a_ews_e) or (ship_col_5_p2 not in ena_ews_pente) or (ship_5_p2 in all_ships_p2): 
        ship_5_p2=input("Invalid position, or position already taken. Try again: ")
        ship_col_5_p2=ship_5_p2[1]
        Ship_row_5_p2=ship_5_p2[0]

    Ship_row_5_p2 = Ship_row_5_p2.lower()
    ship_row_5_p2 = []
    for character in Ship_row_5_p2:
        number = ord(character) - 96
        ship_row_5_p2.append(number)
        ship_row_5_p2=ship_row_5_p2[0]
    ship_row_5_p2=int(ship_row_5_p2)
    ship_col_5_p2=int(ship_col_5_p2)
    all_ships_p2.append(ship_5_p2)

    first_player=random.randint(1,2)
    print("Player " ,first_player,"starts first")
    if first_player==1:
    
        for i in range(500):
            strike_p1= input("Player 1 enter the position to throw your missile:")
            while len(strike_p1)!=2:
                strike_p1=input("Invalid position. Try again:")
            Row_p1=strike_p1[0]
            column_p1=strike_p1[1]

            while (Row_p1 not in a_ews_e) or (column_p1 not in ena_ews_pente):
                strike_p1=input("Invalid position, or missile already thrown there. Try again:")
                Row_p1=strike_p1[0]
                column_p1=strike_p1[1]
            row_p1=[]   
            Row_p1=Row_p1.lower()
            for character in Row_p1:
                number = ord(character) - 96
                row_p1.append(number)
                row_p1=row_p1[0]
            row_p1=int(row_p1)
            column_p1=int(column_p1)

            while (ultra_board2[row_p1][column_p1] == "X") or (ultra_board2[row_p1][column_p1]=="O"):
                strike_p1=input("Invalid position, or missile already thrown there. Try again:")
                Row_p1=strike_p1[0]
                column_p1=strike_p1[1]
                row_p1=[]   
                Row_p1=Row_p1.lower()
                for character in Row_p1:
                    number = ord(character) - 96
                    row_p1.append(number)
                    row_p1=row_p1[0]
                row_p1=int(row_p1)
                column_p1=int(column_p1)

            print("Missile thrown at ",strike_p1)

            if (strike_p1 in all_ships_p2):
                print ("Target hit")
                ultra_board2[row_p1][column_p1] = "O"
                hit_counter_p1=hit_counter_p1+1
                if hit_counter_p1==5:
                    print ("Player 1 wins the game")
                    break

            else:
                print ("Target missed!")
                ultra_board2[row_p1][column_p1] = "X"
        
            board(ultra_board1)
            board(ultra_board2)
            print ("   P1","             P2")
            for i in  range(6):
                print ("".join(ultra_board1[i] ),"        ","".join(ultra_board2[i]))
      
            strike_p2= input("Player 2 enter the position to throw your missile:")
            while len(strike_p2)!=2:
                strike_p2= input("Invalid position. Try again:")
            Row_p2=strike_p2[0]
            column_p2=strike_p2[1]
            while (Row_p2 not in a_ews_e) or (column_p2 not in ena_ews_pente):
                strike_p2= input("Invalid position. Try again:")
                Row_p2=strike_p2[0]
                column_p2=strike_p2[1]
            row_p2=[]   
            Row_p2=Row_p2.lower()
            for character in Row_p2:
                number = ord(character) - 96
                row_p2.append(number)
                row_p2=row_p2[0]
            row_p2=int(row_p2)
            column_p2=int(column_p2)

            while (ultra_board1[row_p2][column_p2] == "X") or (ultra_board1[row_p2][column_p2] == "O"):
                strike_p2=input("Invalid position, or missile already thrown there. Try again:")
                Row_p2=strike_p2[0]
                column_p2=strike_p2[1]
                row_p2=[]
                Row_p2=Row_p2.lower()
                for character in Row_p2:
                    number = ord(character) - 96
                    row_p2.append(number)
                    row_p2=row_p2[0]
                row_p2=int(row_p2)
                column_p2=int(column_p2)
            

            print("Missile thrown at ",strike_p2)
                    
            if (strike_p2 in all_ships_p1):
                print ("Target hit")
                ultra_board1[row_p2][column_p2] = "O"
                hit_counter_p2=hit_counter_p2+1
                if hit_counter_p2==5:
                    print ("Player 2 wins the game")
                    break

            else:
                print ("Target missed!")
                ultra_board1[row_p2][column_p2] = "X"
        
            board(ultra_board1)
            board(ultra_board2)
            print ("   P1","             P2")
            for i in  range(6):
                print ("".join(ultra_board1[i] ),"        ","".join(ultra_board2[i]))
                
    if first_player==2:
        for i in range (500):
            strike_p2= input("Player 2 enter the position to throw your missile:")
            while len(strike_p2)!=2:
                strike_p2= input("Invalid position. Try again:")
            Row_p2=strike_p2[0]
            column_p2=strike_p2[1]
            while (Row_p2 not in a_ews_e) or (column_p2 not in ena_ews_pente):
                strike_p2= input("Invalid position. Try again:")
                Row_p2=strike_p2[0]
                column_p2=strike_p2[1]
            row_p2=[]   
            Row_p2=Row_p2.lower()
            for character in Row_p2:
                number = ord(character) - 96
                row_p2.append(number)
                row_p2=row_p2[0]
            row_p2=int(row_p2)
            column_p2=int(column_p2)

            while (ultra_board1[row_p2][column_p2] == "X") or (ultra_board1[row_p2][column_p2] == "O"):
                strike_p2=input("Invalid position, or missile already thrown there. Try again:")
                Row_p2=strike_p2[0]
                column_p2=strike_p2[1]
            row_p2=[]
            Row_p2=Row_p2.lower()
            for character in Row_p2:
                number = ord(character) - 96
                row_p2.append(number)
                row_p2=row_p2[0]
            row_p2=int(row_p2)
            column_p2=int(column_p2)

            print("Missile thrown at ",strike_p2)
                    
            if (strike_p2 in all_ships_p1):
                print ("Target hit")
                ultra_board1[row_p2][column_p2] = "O"
                hit_counter_p2=hit_counter_p2+1
                if hit_counter_p2==5:
                    print ("Player 2 wins the game")
                    break

            else:
                print ("Target missed!")
                ultra_board1[row_p2][column_p2] = "X"
        
            board(ultra_board1)
            board(ultra_board2)
            print ("   P1","             P2")
            for i in  range(6):
                print ("".join(ultra_board1[i] ),"        ","".join(ultra_board2[i]))
            
                
            strike_p1= input("Player 1 enter the position to throw your missile:")
            while len(strike_p1)!=2:
                strike_p1=input("Invalid position. Try again:")
            Row_p1=strike_p1[0]
            column_p1=strike_p1[1]

            while (Row_p1 not in a_ews_e) or (column_p1 not in ena_ews_pente):
                strike_p1=input("Invalid position, or missile already thrown there. Try again:")
                Row_p1=strike_p1[0]
                column_p1=strike_p1[1]
            row_p1=[]   
            Row_p1=Row_p1.lower()
            for character in Row_p1:
                number = ord(character) - 96
                row_p1.append(number)
                row_p1=row_p1[0]
            row_p1=int(row_p1)
            column_p1=int(column_p1)
            while (ultra_board2[row_p1][column_p1] == "X") or (ultra_board2[row_p1][column_p1]=="O"):
                strike_p1=input("Invalid position, or missile already thrown there. Try again:")
                Row_p1=strike_p1[0]
                column_p1=strike_p1[1]
                row_p1=[]   
                Row_p1=Row_p1.lower()
            for character in Row_p1:
                number = ord(character) - 96
                row_p1.append(number)
                row_p1=row_p1[0]
            row_p1=int(row_p1)
            column_p1=int(column_p1)

            print("Missile thrown at ",strike_p1)

            if (strike_p1 in all_ships_p2):
                print ("Target hit")
                ultra_board2[row_p1][column_p1] = "O"
                hit_counter_p1=hit_counter_p1+1
                if hit_counter_p1==5:
                    print ("Player 1 wins the game")
                    break

            else:
                print ("Target missed!")
                ultra_board2[row_p1][column_p1] = "X"
        
            board(ultra_board1)
            board(ultra_board2)
            print ("   P1","             P2")
            for i in  range(6):
                print ("".join(ultra_board1[i] ),"        ","".join(ultra_board2[i]))

if no_of_players=="1":

    hit_counter_p1=0
    hit_counter_cpu=0
    
    all_ships_p1=[]
    all_ships_cpu=[]
    ship_positions=["a1","a2","a3","a4","a5","b1","b2","b3","b4","b5","c1","c2","c3","c4","c5","d1","d2","d3","d4","d5","e1","e2","e3","e4","e5"]
    ena_ews_pente=["1","2","3","4","5"]
    a_ews_e=["a","b","c","d","e"]
    ship_1_p1=input("Player 1 enter the position of your ship no. 1: ")
    while len(ship_1_p1)!=2:
        ship_1_p1=input("Invalid position. Try again: ")

    ship_col_1_p1=ship_1_p1[1]
    Ship_row_1_p1=ship_1_p1[0]
    while (Ship_row_1_p1 not in a_ews_e) or (ship_col_1_p1 not in ena_ews_pente) :
        ship_1_p1=input("Invalid position. Try again: ")
        ship_col_1_p1=ship_1_p1[1]
        Ship_row_1_p1=ship_1_p1[0]

    Ship_row_1_p1 = Ship_row_1_p1.lower()
    ship_row_1_p1 = []
    for character in Ship_row_1_p1:
        number = ord(character) - 96
        ship_row_1_p1.append(number)
        ship_row_1_p1=ship_row_1_p1[0]
    ship_row_1_p1=int(ship_row_1_p1)
    ship_col_1_p1=int(ship_col_1_p1)
    all_ships_p1.append(ship_1_p1)

    ship_2_p1=input("Player 1 enter the position of your ship no. 2: ")
    while len(ship_2_p1)!=2:
        ship_2_p1=input("Invalid position. Try again: ")

    ship_col_2_p1=ship_2_p1[1]
    Ship_row_2_p1=ship_2_p1[0]
    while (Ship_row_2_p1 not in a_ews_e) or (ship_col_2_p1 not in ena_ews_pente) or (ship_2_p1 in all_ships_p1):
        ship_2_p1=input("Invalid position, or position already taken. Try again: ")
        ship_col_2_p1=ship_2_p1[1]
        Ship_row_2_p1=ship_2_p1[0]

    Ship_row_2_p1 = Ship_row_2_p1.lower()
    ship_row_2_p1 = []
    for character in Ship_row_2_p1:
        number = ord(character) - 96
        ship_row_2_p1.append(number)
        ship_row_2_p1=ship_row_2_p1[0]
        ship_col_1_p1=ship_2_p1[1]
    ship_row_2_p1=int(ship_row_2_p1)
    ship_col_2_p1=int(ship_col_2_p1)
    all_ships_p1.append(ship_2_p1)

    ship_3_p1=input("Player 1 enter the position of your ship no. 3: ")
    while len(ship_3_p1)!=2:
        ship_3_p1=input("Invalid position. Try again: ")

    ship_col_3_p1=ship_3_p1[1]
    Ship_row_3_p1=ship_3_p1[0]
    while (Ship_row_3_p1 not in a_ews_e) or (ship_col_3_p1 not in ena_ews_pente) or (ship_3_p1 in all_ships_p1):
        ship_3_p1=input("Invalid position, or position already taken. Try again: ")
        ship_col_3_p1=ship_3_p1[1]
        Ship_row_3_p1=ship_3_p1[0]

    Ship_row_3_p1 = Ship_row_3_p1.lower()
    ship_row_3_p1 = []
    for character in Ship_row_3_p1:
        number = ord(character) - 96
        ship_row_3_p1.append(number)
        ship_row_3_p1=ship_row_3_p1[0]
        ship_col_3_p1=ship_3_p1[1]
    ship_row_3_p1=int(ship_row_3_p1)
    ship_col_3_p1=int(ship_col_3_p1)
    all_ships_p1.append(ship_3_p1)

    ship_4_p1=input("Player 1 enter the position of your ship no. 4: ")
    while len(ship_4_p1)!=2:
        ship_4_p1=input("Invalid position. Try again: ")

    ship_col_4_p1=ship_4_p1[1]
    Ship_row_4_p1=ship_4_p1[0]
    while (Ship_row_4_p1 not in a_ews_e) or (ship_col_4_p1 not in ena_ews_pente) or (ship_4_p1 in all_ships_p1):
        ship_4_p1=input("Invalid position, or position already taken. Try again: ")
        ship_col_4_p1=ship_4_p1[1]
        Ship_row_4_p1=ship_4_p1[0]

    Ship_row_4_p1 = Ship_row_4_p1.lower()
    ship_row_4_p1 = []
    for character in Ship_row_4_p1:
        number = ord(character) - 96
        ship_row_4_p1.append(number)
        ship_row_4_p1=ship_row_4_p1[0]
    ship_row_4_p1=int(ship_row_4_p1)
    ship_col_4_p1=int(ship_col_4_p1)
    all_ships_p1.append(ship_4_p1)

    ship_5_p1=input("Player 1 enter the position of your ship no. 5: ")
    while len(ship_5_p1)!=2:
        ship_5_p1=input("Invalid position. Try again: ")

    ship_col_5_p1=ship_5_p1[1]
    Ship_row_5_p1=ship_5_p1[0]
    while (Ship_row_5_p1 not in a_ews_e) or (ship_col_5_p1 not in ena_ews_pente) or (ship_5_p1 in all_ships_p1):
        ship_5_p1=input("Invalid position, or position already taken. Try again: ")
        ship_col_5_p1=ship_5_p1[1]
        Ship_row_5_p1=ship_5_p1[0]

    Ship_row_5_p1 = Ship_row_5_p1.lower()
    ship_row_5_p1 = []
    for character in Ship_row_5_p1:
        number = ord(character) - 96
        ship_row_5_p1.append(number)
        ship_row_5_p1=ship_row_5_p1[0]
    ship_row_5_p1=int(ship_row_5_p1)
    ship_col_5_p1=int(ship_col_5_p1)
    all_ships_p1.append(ship_5_p1)
    
    ship_1_cpu=random.choice(ship_positions)
    all_ships_cpu.append(ship_1_cpu)
    
    ship_2_cpu=random.choice(ship_positions)
    all_ships_cpu.append(ship_2_cpu)
    
    ship_3_cpu=random.choice(ship_positions)
    all_ships_cpu.append(ship_3_cpu)
    
    ship_4_cpu=random.choice(ship_positions)
    all_ships_cpu.append(ship_4_cpu)
    
    ship_5_cpu=random.choice(ship_positions)
    all_ships_cpu.append(ship_5_cpu)
    
    first_player=random.randint(1,2)
    if first_player==1:
        print("Player " ,first_player,"starts first")
    
        for i in range(500):
            strike_p1= input("Player 1 enter the position to throw your missile:")
            while len(strike_p1)!=2:
                strike_p1=input("Invalid position. Try again:")
            Row_p1=strike_p1[0]
            column_p1=strike_p1[1]

            while (Row_p1 not in a_ews_e) or (column_p1 not in ena_ews_pente):
                strike_p1=input("Invalid position, or missile already thrown there. Try again:")
                Row_p1=strike_p1[0]
                column_p1=strike_p1[1]
            row_p1=[]   
            Row_p1=Row_p1.lower()
            for character in Row_p1:
                number = ord(character) - 96
                row_p1.append(number)
                row_p1=row_p1[0]
            row_p1=int(row_p1)
            column_p1=int(column_p1)

            while (ultra_board2[row_p1][column_p1] == "X") or (ultra_board2[row_p1][column_p1]=="O"):
                strike_p1=input("Invalid position, or missile already thrown there. Try again:")
                Row_p1=strike_p1[0]
                column_p1=strike_p1[1]
                row_p1=[]   
                Row_p1=Row_p1.lower()
                for character in Row_p1:
                    number = ord(character) - 96
                    row_p1.append(number)
                    row_p1=row_p1[0]
                row_p1=int(row_p1)
                column_p1=int(column_p1)

            print("Missile thrown at ",strike_p1)

            if (strike_p1 in all_ships_cpu):
                print ("Target hit")
                ultra_board2[row_p1][column_p1] = "O"
                hit_counter_p1=hit_counter_p1+1
                if hit_counter_p1==5:
                    print ("Player 1 wins the game")
                    break

            else:
                print ("Target missed!")
                ultra_board2[row_p1][column_p1] = "X"
        
            board(ultra_board1)
            board(ultra_board2)
            print ("   P1","             CPU")
            for i in  range(6):
                print ("".join(ultra_board1[i] ),"        ","".join(ultra_board2[i]))
                
            
            strike_cpu=random.choice(ship_positions)
            Row_cpu=strike_cpu[0]
            column_cpu=strike_cpu[1]
            row_cpu=[]
            for character in Row_cpu:
                number=ord(character)-96
                row_cpu.append(number)
                row_cpu=row_cpu[0]
            row_cpu=int(row_cpu)
            column_cpu=int(column_cpu)

            while (ultra_board1[row_cpu][column_cpu] == "X") or (ultra_board1[row_cpu][column_cpu]=="O"):
                strike_cpu=random.choice(ship_positions)
                Row_cpu=strike_cpu[0]
                column_cpu=strike_cpu[1]
                row_cpu=[]
                for character in Row_cpu:
                    number=ord(character)-96
                    row_cpu.append(number)
                    row_cpu=row_cpu[0]
                row_cpu=int(row_cpu)
                column_cpu=int(column_cpu)

            print("Missile thrown at ",strike_cpu)

            if (strike_cpu in all_ships_p1):
                print ("Target hit")
                ultra_board1[row_cpu][column_cpu] = "O"
                hit_counter_cpu=hit_counter_cpu+1
                if hit_counter_cpu==5:
                    print ("CPU wins the game")
                    break

            else:
                print ("Target missed!")
                ultra_board1[row_cpu][column_cpu] = "X"
        
            board(ultra_board1)
            board(ultra_board2)
            print ("   P1","             CPU")
            for i in  range(6):
                print ("".join(ultra_board1[i] ),"        ","".join(ultra_board2[i]))
                

    if first_player==2:
        print("CPU starts first")
    
        for i in range(500):
            strike_cpu=random.choice(ship_positions)
            Row_cpu=strike_cpu[0]
            column_cpu=strike_cpu[1]
            row_cpu=[]
            for character in Row_cpu:
                number=ord(character)-96
                row_cpu.append(number)
                row_cpu=row_cpu[0]
            row_cpu=int(row_cpu)
            column_cpu=int(column_cpu)

            while (ultra_board1[row_cpu][column_cpu] == "X") or (ultra_board1[row_cpu][column_cpu]=="O"):
                strike_cpu=random.choice(ship_positions)
                Row_cpu=strike_cpu[0]
                column_cpu=strike_cpu[1]
                row_cpu=[]
                for character in Row_cpu:
                    number=ord(character)-96
                    row_cpu.append(number)
                    row_cpu=row_cpu[0]
                row_cpu=int(row_cpu)
                column_cpu=int(column_cpu)

            print("Missile thrown at ",strike_cpu)

            if (strike_cpu in all_ships_p1):
                print ("Target hit")
                ultra_board1[row_cpu][column_cpu] = "O"
                hit_counter_cpu=hit_counter_cpu+1
                if hit_counter_cpu==5:
                    print ("CPU wins the game")
                    break

            else:
                print ("Target missed!")
                ultra_board1[row_cpu][column_cpu] = "X"
        
            board(ultra_board1)
            board(ultra_board2)
            print ("   P1","             CPU")
            for i in  range(6):
                print ("".join(ultra_board1[i] ),"        ","".join(ultra_board2[i]))
                
                
            strike_p1= input("Player 1 enter the position to throw your missile:")
            while len(strike_p1)!=2:
                strike_p1=input("Invalid position. Try again:")
            Row_p1=strike_p1[0]
            column_p1=strike_p1[1]

            while (Row_p1 not in a_ews_e) or (column_p1 not in ena_ews_pente):
                strike_p1=input("Invalid position, or missile already thrown there. Try again:")
                Row_p1=strike_p1[0]
                column_p1=strike_p1[1]
            row_p1=[]   
            Row_p1=Row_p1.lower()
            for character in Row_p1:
                number = ord(character) - 96
                row_p1.append(number)
                row_p1=row_p1[0]
            row_p1=int(row_p1)
            column_p1=int(column_p1)

            while (ultra_board2[row_p1][column_p1] == "X") or (ultra_board2[row_p1][column_p1]=="O"):
                strike_p1=input("Invalid position, or missile already thrown there. Try again:")
                Row_p1=strike_p1[0]
                column_p1=strike_p1[1]
                row_p1=[]   
                Row_p1=Row_p1.lower()
                for character in Row_p1:
                    number = ord(character) - 96
                    row_p1.append(number)
                    row_p1=row_p1[0]
                row_p1=int(row_p1)
                column_p1=int(column_p1)

            print("Missile thrown at ",strike_p1)

            if (strike_p1 in all_ships_cpu):
                print ("Target hit")
                ultra_board2[row_p1][column_p1] = "O"
                hit_counter_p1=hit_counter_p1+1
                if hit_counter_p1==5:
                    print ("Player 1 wins the game")
                    break

            else:
                print ("Target missed!")
                ultra_board2[row_p1][column_p1] = "X"
        
            board(ultra_board1)
            board(ultra_board2)
            print ("   P1","             CPU")
            for i in  range(6):
                print ("".join(ultra_board1[i] ),"        ","".join(ultra_board2[i]))
				
# mou bgike "ligo" megaliteri apo oso tha eprepe alla mou arese i idea kai lew krima einai
#alla telika
#den itan krima epeidi bgike ergasia 800 seires