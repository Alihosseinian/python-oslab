import random
import os
from colorama import Fore
import datetime
a = datetime.datetime.now()
 
#####################################################################################################

def show_game_board():
    for i in range(3):
        for j in range(3): 
            if game[i][j]=="y" : 
                print(Fore.RED + game[i][j]  + Fore.RESET , end=' '  )
            if game[i][j]=="x":
                print( Fore.BLUE + game[i][j]  + Fore.RESET , end=' ' )
            if game[i][j]=="-":
                 print( Fore.WHITE + game[i][j] + Fore.RESET, end=' ' )
        print()

#####################################################################################################

def check_game_winner ():
    if ((game[0][0]=="x" and game[0][1]=="x" and game[0][2]=="x")  or
        (game[1][0]=="x" and game[1][1]=="x" and game[1][2]=="x" ) or
        (game[2][0]=="x" and game[2][1]=="x" and game[2][2]=="x" ) or
        (game[0][0]=="x" and game[1][0]=="x" and game[2][0]=="x" ) or
        (game[0][1]=="x" and game[1][1]=="x" and game[2][1]=="x" ) or
        (game[0][2]=="x" and game[1][2]=="x" and game[2][2]=="x" ) or
        (game[0][0]=="x" and game[1][1]=="x" and game[2][2]=="x" ) or
        (game[0][2]=="x" and game[1][1]=="x" and game[2][0]=="x" )) :
        print("winner : player 1 \n")
        b = datetime.datetime.now()
        c = b - a
        print("modat zaman bazi : " , int(c.total_seconds() * 1000))
        return True
    elif ((game[0][0]=="y" and game[0][1]=="y" and game[0][2]=="y") or
        (game[1][0]=="y" and game[1][1]=="y" and game[1][2]=="y"  ) or
        (game[2][0]=="y" and game[2][1]=="y" and game[2][2]=="y" )  or
        (game[0][0]=="y" and game[1][0]=="y" and game[2][0]=="y" )  or
        (game[0][1]=="y" and game[1][1]=="y" and game[2][1]=="y" )  or
        (game[0][2]=="y" and game[1][2]=="y" and game[2][2]=="y" )  or
        (game[0][0]=="y" and game[1][1]=="y" and game[2][2]=="v" )  or
        (game[0][2]=="y" and game[1][1]=="y" and game[2][0]=="y" )) :
        print("winner : player 2 \n")
        b = datetime.datetime.now()
        c = b - a
        print("modat zaman bazi : " , int(c.total_seconds() * 1000))
        return True
    
#####################################################################################################

def do_nafare  ():
    #player 1
    while True :
        while True : 
            print("\n player 1","\n")
            satr=int(input("lotfan satr mored nazar ra vared konid : "))-1
            soton=int(input("lotfan soton mored nazar ra vared konid : "))-1
            if 0 <= satr <= 2 and 0 <= soton <= 2 :
                if game[satr][soton] == "-" :
                    game[satr][soton] = "x"
                    show_game_board()
                    finished_game=check_game_winner ()
                    break
                else :
                    print("in khane ghabln entekhab shode ast ")
            else : 
                print("lotfan adadi bein 1-3 vared konid ")    
        if finished_game : 
            break    
        #player 2
        while True : 
            print("\n player 2","\n")
            satr=int(input("lotfan satr mored nazar ra vared konid : "))-1
            soton=int(input("lotfan soton mored nazar ra vared konid : "))-1
            if 0 <= satr <= 2 and 0 <= soton <= 2 :
                if game[satr][soton] == "-" :
                    game[satr][soton] = "y"
                    show_game_board()
                    finished_game=check_game_winner ()
                    break
                else:
                    print("in khane ghabln entekhab shode ast ")
            else : 
                print("lotfan adadi bein 1-3 vared konid ")    
        if finished_game : 
            break    

########################################################################################################

def tak_nafare ():
    #player 1
        while True :
            while True : 
                print("\n player 1","\n")
                satr=int(input("lotfan satr mored nazar ra vared konid : "))-1
                soton=int(input("lotfan soton mored nazar ra vared konid : "))-1
                if 0 <= satr <= 2 and 0 <= soton <= 2 :
                    if game[satr][soton] == "-" :
                        game[satr][soton] = "x"
                        show_game_board()
                        finished_game=check_game_winner ()
                        break
                    else :
                        print("in khane ghabln entekhab shode ast ")
                else : 
                    print("lotfan adadi bein 1-3 vared konid ")    
            if finished_game : 
                break        
            #player 2 (computer )
            while True : 
                print("\n player 2 (computer ) ","\n")
                satr=random.randint(0,2)
                soton=random.randint(0,2)
                if 0 <= satr <= 2 and 0 <= soton <= 2 :
                    if game[satr][soton] == "-" :
                        game[satr][soton] = "y"
                        show_game_board()
                        finished_game=check_game_winner ()
                        break   
            if finished_game : 
                break    

########################################################################################################
#main()
os.system("cls")

game=[[ '-' , '-' , '-'],
      [ '-' , '-' , '-'],
      [ '-' , '-' , '-']]

show_game_board()
print ("welcome \n")
while True : 
    print ("\n[ 1 : tak nafare ]\n[ 2 : do nafare ]\n[ 3 : exit ]\n")
    nahve=int (input ("nahve bazi ra entekhab konid : "))
    if nahve == 1 :
        tak_nafare ()
    if nahve == 2 :
        do_nafare ()
    if nahve == 3 :  
        print("goodby :) \n")
        break
########################################################################################################