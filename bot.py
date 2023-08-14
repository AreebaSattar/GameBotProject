import sys; print(sys.path)
from command import Command
from game_state import GameState
from player import Player
import numpy as np
import pandas as pd
from buttons import Buttons
import sklearn
from sklearn.preprocessing import StandardScaler

import joblib
class Bot:

    def __init__(self):
        #< - v + < - v - v + > - > + Y
        self.fire_code=["<","!<","v+<","!v+!<","v","!v","v+>","!v+!>",">+Y","!>+!Y"]
        self.exe_code = 0
        self.start_fire=True
        self.remaining_code=[]
        self.my_command = Command()
        self.buttn= Buttons()

    def fight(self,current_game_state,player):
        #python Videos\gamebot-competition-master\PythonAPI\controller.py 1
        model = joblib.load("Model.joblib")
        # diff=current_game_state.player1.x_coord - current_game_state.player2.x_coord
        Pl1_Hlth=current_game_state.player1.health
        pl2_Hlth=current_game_state.player2.health
        diff=current_game_state.player1.x_coord - current_game_state.player2.x_coord
        
        p1_is_jumpingg=current_game_state.player1.is_jumping 
        p2_isjumping=current_game_state.player2.is_jumping 
        p1is_crouching=current_game_state.player1.is_crouching
        p2_is_crouching=current_game_state.player2.is_crouching
        p1move=current_game_state.player1.is_player_in_move
        p2_move=current_game_state.player2.is_player_in_move
        pl2_id=current_game_state.player2.player_id
        p1_ids=current_game_state.player1.player_id
        p1_move_ids=current_game_state.player1.move_id
        p2_moveid=current_game_state.player2.move_id
        features = [[Pl1_Hlth, pl2_Hlth,p1_is_jumpingg,p1is_crouching,p1move,p1_move_ids, p1_ids, pl2_id,p2_isjumping,p2_is_crouching,p2_move,p2_moveid]]

        
        SolPredVa = model.predict(features)
        #print(SolPredVa)
       
           
        if player=="1":            
        
            self.buttn.up=int(SolPredVa[0][0])
            self.buttn.down=int(SolPredVa[0][1])
            self.buttn.right=int(SolPredVa[0][2])
            self.buttn.left=int(SolPredVa[0][3])
            self.buttn.X=int(SolPredVa[0][4])
            self.buttn.Y=int(SolPredVa[0][5])
            self.buttn.A=int(SolPredVa[0][6])
            self.buttn.B=int(SolPredVa[0][7])
            self.buttn.L=int(SolPredVa[0][8])
            self.buttn.R=int(SolPredVa[0][9])
            self.my_command.player_buttons =self.buttn

        elif player=="2":

            self.buttn.up=int(SolPredVa[0][0])
            self.buttn.down=int(SolPredVa[0][1])
            self.buttn.right=int(SolPredVa[0][2])
            self.buttn.left=int(SolPredVa[0][3])
            self.buttn.X=int(SolPredVa[0][4])
            self.buttn.Y=int(SolPredVa[0][5])
            self.buttn.A=int(SolPredVa[0][6])
            self.buttn.B=int(SolPredVa[0][7])
            self.buttn.L=int(SolPredVa[0][8])
            self.buttn.R=int(SolPredVa[0][9])
            self.my_command.player_buttons =self.buttn
        return self.my_command

    def run_command( self , com , player   ):

        if self.exe_code-1==len(self.fire_code):
            self.exe_code=0
            self.start_fire=False
            print ("compelete")
            #exit()
            # print ( "left:",player.player_buttons.left )
            # print ( "right:",player.player_buttons.right )
            # print ( "up:",player.player_buttons.up )
            # print ( "down:",player.player_buttons.down )
            # print ( "Y:",player.player_buttons.Y )

        elif len(self.remaining_code)==0 :

            self.fire_code=com
            #self.my_command=Command()
            self.exe_code+=1

            self.remaining_code=self.fire_code[0:]

        else:
            self.exe_code+=1
            if self.remaining_code[0]=="v+<":
                self.buttn.down=True
                self.buttn.left=True
                print("v+<")
            elif self.remaining_code[0]=="!v+!<":
                self.buttn.down=False
                self.buttn.left=False
                print("!v+!<")
            elif self.remaining_code[0]=="v+>":
                self.buttn.down=True
                self.buttn.right=True
                print("v+>")
            elif self.remaining_code[0]=="!v+!>":
                self.buttn.down=False
                self.buttn.right=False
                print("!v+!>")

            elif self.remaining_code[0]==">+Y":
                self.buttn.Y= True #not (player.player_buttons.Y)
                self.buttn.right=True
                print(">+Y")
            elif self.remaining_code[0]=="!>+!Y":
                self.buttn.Y= False #not (player.player_buttons.Y)
                self.buttn.right=False
                print("!>+!Y")

            elif self.remaining_code[0]=="<+Y":
                self.buttn.Y= True #not (player.player_buttons.Y)
                self.buttn.left=True
                print("<+Y")
            elif self.remaining_code[0]=="!<+!Y":
                self.buttn.Y= False #not (player.player_buttons.Y)
                self.buttn.left=False
                print("!<+!Y")

            elif self.remaining_code[0]== ">+^+L" :
                self.buttn.right=True
                self.buttn.up=True
                self.buttn.L= not (player.player_buttons.L)
                print(">+^+L")
            elif self.remaining_code[0]== "!>+!^+!L" :
                self.buttn.right=False
                self.buttn.up=False
                self.buttn.L= False #not (player.player_buttons.L)
                print("!>+!^+!L")

            elif self.remaining_code[0]== ">+^+Y" :
                self.buttn.right=True
                self.buttn.up=True
                self.buttn.Y= not (player.player_buttons.Y)
                print(">+^+Y")
            elif self.remaining_code[0]== "!>+!^+!Y" :
                self.buttn.right=False
                self.buttn.up=False
                self.buttn.Y= False #not (player.player_buttons.L)
                print("!>+!^+!Y")


            elif self.remaining_code[0]== ">+^+R" :
                self.buttn.right=True
                self.buttn.up=True
                self.buttn.R= not (player.player_buttons.R)
                print(">+^+R")
            elif self.remaining_code[0]== "!>+!^+!R" :
                self.buttn.right=False
                self.buttn.up=False
                self.buttn.R= False #ot (player.player_buttons.R)
                print("!>+!^+!R")

            elif self.remaining_code[0]== ">+^+A" :
                self.buttn.right=True
                self.buttn.up=True
                self.buttn.A= not (player.player_buttons.A)
                print(">+^+A")
            elif self.remaining_code[0]== "!>+!^+!A" :
                self.buttn.right=False
                self.buttn.up=False
                self.buttn.A= False #not (player.player_buttons.A)
                print("!>+!^+!A")

            elif self.remaining_code[0]== ">+^+B" :
                self.buttn.right=True
                self.buttn.up=True
                self.buttn.B= not (player.player_buttons.B)
                print(">+^+B")
            elif self.remaining_code[0]== "!>+!^+!B" :
                self.buttn.right=False
                self.buttn.up=False
                self.buttn.B= False #not (player.player_buttons.A)
                print("!>+!^+!B")

            elif self.remaining_code[0]== "<+^+L" :
                self.buttn.left=True
                self.buttn.up=True
                self.buttn.L= not (player.player_buttons.L)
                print("<+^+L")
            elif self.remaining_code[0]== "!<+!^+!L" :
                self.buttn.left=False
                self.buttn.up=False
                self.buttn.L= False  #not (player.player_buttons.Y)
                print("!<+!^+!L")

            elif self.remaining_code[0]== "<+^+Y" :
                self.buttn.left=True
                self.buttn.up=True
                self.buttn.Y= not (player.player_buttons.Y)
                print("<+^+Y")
            elif self.remaining_code[0]== "!<+!^+!Y" :
                self.buttn.left=False
                self.buttn.up=False
                self.buttn.Y= False  #not (player.player_buttons.Y)
                print("!<+!^+!Y")

            elif self.remaining_code[0]== "<+^+R" :
                self.buttn.left=True
                self.buttn.up=True
                self.buttn.R= not (player.player_buttons.R)
                print("<+^+R")
            elif self.remaining_code[0]== "!<+!^+!R" :
                self.buttn.left=False
                self.buttn.up=False
                self.buttn.R= False  #not (player.player_buttons.Y)
                print("!<+!^+!R")

            elif self.remaining_code[0]== "<+^+A" :
                self.buttn.left=True
                self.buttn.up=True
                self.buttn.A= not (player.player_buttons.A)
                print("<+^+A")
            elif self.remaining_code[0]== "!<+!^+!A" :
                self.buttn.left=False
                self.buttn.up=False
                self.buttn.A= False  #not (player.player_buttons.Y)
                print("!<+!^+!A")

            elif self.remaining_code[0]== "<+^+B" :
                self.buttn.left=True
                self.buttn.up=True
                self.buttn.B= not (player.player_buttons.B)
                print("<+^+B")
            elif self.remaining_code[0]== "!<+!^+!B" :
                self.buttn.left=False
                self.buttn.up=False
                self.buttn.B= False  #not (player.player_buttons.Y)
                print("!<+!^+!B")

            elif self.remaining_code[0]== "v+R" :
                self.buttn.down=True
                self.buttn.R= not (player.player_buttons.R)
                print("v+R")
            elif self.remaining_code[0]== "!v+!R" :
                self.buttn.down=False
                self.buttn.R= False  #not (player.player_buttons.Y)
                print("!v+!R")

            else:
                if self.remaining_code[0] =="v" :
                    self.buttn.down=True
                    print ( "down" )
                elif self.remaining_code[0] =="!v":
                    self.buttn.down=False
                    print ( "Not down" )
                elif self.remaining_code[0] =="<" :
                    print ( "left" )
                    self.buttn.left=True
                elif self.remaining_code[0] =="!<" :
                    print ( "Not left" )
                    self.buttn.left=False
                elif self.remaining_code[0] ==">" :
                    print ( "right" )
                    self.buttn.right=True
                elif self.remaining_code[0] =="!>" :
                    print ( "Not right" )
                    self.buttn.right=False

                elif self.remaining_code[0] =="^" :
                    print ( "up" )
                    self.buttn.up=True
                elif self.remaining_code[0] =="!^" :
                    print ( "Not up" )
                    self.buttn.up=False
            self.remaining_code=self.remaining_code[1:]
        return
# col=['diff','action','player']
# df=pd.DataFrame(columns=col)
# bot = Bot()
# for i in range(100):
#     curen_G_state = GameState(input_dict)
#     curen_G_state.player1 = Player() 
#     curen_G_state.player2 = Player() 
#     dif= curen_G_state.player2.x_coord-curen_G_state.player1.x_coord
#     act=bot.fight (curen_G_state,curen_G_state.player1) 
#     df=df.append({'diff':dif,'action':act,'player':curen_G_state.player1},ignore_index=True)
#     #df.loc[i]=[bot.diff,bot.action,bot.player]
# df.to_csv('bot.csv')