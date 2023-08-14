import socket
import json
from game_state import GameState
import pandas as pd
import pandas as pd
import joblib

#from bot import fight
import sys
from bot import Bot
def connect(port):
    #For making a connection with the game
    server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server_socket.bind(("127.0.0.1", port))
    server_socket.listen(5)
    (client_socket, _) = server_socket.accept()
    print ("Connected to game!")
    return client_socket

def send(client_socket, command):
    #This function will send your updated command to Bizhawk so that game reacts according to your command.
    command_dict = command.object_to_dict()
    pay_load = json.dumps(command_dict).encode()
    client_socket.sendall(pay_load)

def receive(client_socket):
    #receive the game state and return game state
    pay_load = client_socket.recv(4096)
    input_dict = json.loads(pay_load.decode())
    game_state = GameState(input_dict)

    return game_state

def main():
    if (sys.argv[1]=='1'):
        client_socket = connect(9999)
    elif (sys.argv[1]=='2'):
        client_socket = connect(10000)
    current_game_state = None
    #print( current_game_state.is_round_over )
    bot=Bot()
    HeaderValsC=['timer','fight_result','has_round_started','is_round_over','Player1_ID','Player1_health','Player1_x_coord','Player1_y_coord','Player1_is_jumping','Player1_is_crouching','Player1_is_player_in_move','Player1_move_id','Player1_buttons_up','Player1_buttons_down','Player1_buttons_right','Player1_buttons_left','Player1_buttons_X','Player1_buttons_Y','Player1_buttons_A','Player1_buttons_B','Player1_buttons_L','Player1_buttons_R','Player2_ID','Player2_health','Player2_x_coord','Player2_y_coord','Player2_is_jumping','Player2_is_crouching','Player2_is_player_in_move','Player2_move_id','Player2_buttons_up','Player2_buttons_down','Player2_buttons_right','Player2_buttons_left','Player2_buttons_X','Player2_buttons_Y','Player2_buttons_A','Player2_buttons_B','Player2_buttons_L','Player2_buttons_R']
    Val_df=pd.DataFrame(columns=HeaderValsC)
    while (current_game_state is None) or (not current_game_state.is_round_over):

        current_game_state = receive(client_socket)
        bot_command = bot.fight(current_game_state,sys.argv[1])
        
        checked = bot_command.object_to_dict()
        #print("bot_command",checked)
        timer =current_game_state.timer
        fight_result=current_game_state.fight_result
        has_round_S=current_game_state.has_round_started
        is_round_overr=current_game_state.is_round_over
        Player1_IDd=current_game_state.player1.player_id
        Player1_health=current_game_state.player1.health
        Player1_x_coord=current_game_state.player1.x_coord
        Player1_y_coord=current_game_state.player1.y_coord
        Player1_is_jumping=current_game_state.player1.is_jumping
        Player1_is_crouching=current_game_state.player1.is_crouching
        Player1_is_player_in_move=current_game_state.player1.is_player_in_move
        Player1_move_id=current_game_state.player1.move_id
        Player1_buttons_up=current_game_state.player1.player_buttons.up
        Player1_buttons_down=current_game_state.player1.player_buttons.down
        Player1_buttons_right=current_game_state.player1.player_buttons.right
        Player1_buttons_left=current_game_state.player1.player_buttons.left
        Player1_buttons_X=current_game_state.player1.player_buttons.X
        Player1_buttons_Y=current_game_state.player1.player_buttons.Y
        Player1_buttons_A=current_game_state.player1.player_buttons.A
        Player1_buttons_B=current_game_state.player1.player_buttons.B
        Player1_buttons_L=current_game_state.player1.player_buttons.L
        Player1_buttons_R=current_game_state.player1.player_buttons.R
        Player2_ID=current_game_state.player2.player_id
        Player2_health=current_game_state.player2.health
        Player2_x_coord=current_game_state.player2.x_coord
        Player2_y_coord=current_game_state.player2.y_coord
        Player2_is_jumping=current_game_state.player2.is_jumping
        Player2_is_crouching=current_game_state.player2.is_crouching
        Player2_is_player_in_move=current_game_state.player2.is_player_in_move
        Player2_move_id=current_game_state.player2.move_id
        Player2_buttons_up=current_game_state.player2.player_buttons.up
        Player2_buttons_down=current_game_state.player2.player_buttons.down
        Player2_buttons_right=current_game_state.player2.player_buttons.right
        Player2_buttons_left=current_game_state.player2.player_buttons.left
        Player2_buttons_X=current_game_state.player2.player_buttons.X
        Player2_buttons_Y=current_game_state.player2.player_buttons.Y
        Player2_buttons_A=current_game_state.player2.player_buttons.A
        Player2_buttons_B=current_game_state.player2.player_buttons.B
        Player2_buttons_L=current_game_state.player2.player_buttons.L
        Player2_buttons_R=current_game_state.player2.player_buttons.R
        
        
        
        Val_df= pd.concat([Val_df,pd.DataFrame([{'timer':timer,'fight_result':fight_result,'has_round_started':has_round_S,
                                         'is_round_over':is_round_overr,'Player1_ID':Player1_IDd,
                                         'Player1_health':Player1_health,'Player1_x_coord':Player1_x_coord,
                                         'Player1_y_coord':Player1_y_coord,
                                         'Player1_is_jumping':Player1_is_jumping,'Player1_is_crouching':Player1_is_crouching,
                                         'Player1_is_player_in_move':Player1_is_player_in_move,
                                         'Player1_move_id':Player1_move_id,
                                         'Player1_buttons_up':Player1_buttons_up,
                                         'Player1_buttons_down':Player1_buttons_down,
                                         'Player1_buttons_right':Player1_buttons_right,
                                         'Player1_buttons_left':Player1_buttons_left,
                                         'Player1_buttons_X':Player1_buttons_X,
                                         'Player1_buttons_Y':Player1_buttons_Y,
                                         'Player1_buttons_A':Player1_buttons_A,
                                         'Player1_buttons_B':Player1_buttons_B,
                                         'Player1_buttons_L':Player1_buttons_L,
                                         'Player1_buttons_R':Player1_buttons_R,
                                         'Player2_ID':Player2_ID,
                                         'Player2_health':Player2_health,
                                         'Player2_x_coord':Player2_x_coord,
                                         'Player2_y_coord':Player2_y_coord,
                                         'Player2_is_jumping':Player2_is_jumping,'Player2_is_crouching':Player2_is_crouching,
                                         'Player2_is_player_in_move':Player2_is_player_in_move,
                                         'Player2_move_id':Player2_move_id,
                                         'Player2_buttons_up':Player2_buttons_up,
                                         'Player2_buttons_down':Player2_buttons_down,
                                         'Player2_buttons_right':Player2_buttons_right,
                                         'Player2_buttons_left':Player2_buttons_left,
                                         'Player2_buttons_X':Player2_buttons_X,
                                         'Player2_buttons_Y':Player2_buttons_Y,
                                         'Player2_buttons_A':Player2_buttons_A,
                                         'Player2_buttons_B':Player2_buttons_B,
                                         'Player2_buttons_L':Player2_buttons_L,
                                         'Player2_buttons_R':Player2_buttons_R
                                         
                                         }])],ignore_index=True)
        send(client_socket, bot_command)
    print(pd.__version__)
    #df.to_csv('uff.csv',index=False,header=True,mode='a')
    
   
if __name__ == '__main__':
   main()

'''
        #dif= current_game_state.player2.x_coord-current_game_state.player1.x_coord
        print("health1",health1)
        print("health2",health2)
        print("timer",timer)
        print("fight_result",fight_result)
        print("has_round_S",has_round_S)
        print("is_round_over",is_round_overr)
        print("Player1_ID",Player1_IDd)
        print("Player1_health",Player1_health)
        print("Player1_x_coord",Player1_x_coord)
        print("Player1_y_coord",Player1_y_coord)
        print("Player1_is_jumping",Player1_is_jumping)
        print("Player1_is_crouching",Player1_is_crouching)
        print("Player1_is_player_in_move",Player1_is_player_in_move)
        print("Player1_move_id",Player1_move_id)
        print("Player1_buttons_up",Player1_buttons_up)
        print("Player1_buttons_down",Player1_buttons_down)
        print("Player1_buttons_right",Player1_buttons_right)
        print("Player1_buttons_left",Player1_buttons_left)
        print("Player2_ID",Player2_ID)
        print("Player2_health",Player2_health)
        print("Player2_x_coord",Player2_x_coord)
        print("Player2_y_coord",Player2_y_coord)
        print("Player2_is_jumping",Player2_is_jumping)
        print("Player2_is_crouching",Player2_is_crouching)
        print("Player2_is_player_in_move",Player2_is_player_in_move)
        print("Player2_move_id",Player2_move_id)
        print("Player2_buttons_up",Player2_buttons_up)
        print("Player2_buttons_down",Player2_buttons_down)
        print("Player2_buttons_right",Player2_buttons_right)
        print("Player2_buttons_left",Player2_buttons_left)'''


