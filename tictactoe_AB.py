from pade.core.agent import Agent
from pade.acl.aid import AID
from pade.misc.utility import display_message , start_loop
from pade.acl.messages import ACLMessage
import sys
import time

#"O" for Computer and "X" for Human
#initializing board
board = [['_','_','_'],['_','_','_'],['_','_','_']]

def print_board():
    for i in range(3):
        j=0
        print(board[i][j] + '  ' + board[i][j+1] + '  ' + board[i][j+2])
   
def finished():
    #column win
    for i in range(0, 3):
        if (board[0][i] != ' ' and board[0][i] == board[1][i] and board[1][i] == board[2][i]):
            return board[0][i]

    #row win
    for i in range(0, 3):
        if (board[i] == ['X', 'X', 'X']):
            return 'X'
        elif (board[i] == ['O', 'O', 'O']):
            return 'O'

    #diagnols win
    if (board[0][0] != '_' and board[0][0] == board[1][1] and board[0][0] == board[2][2]):
        return board[0][0]

    if (board[0][2] != '_' and board[0][2] == board[1][1] and board[0][2] == board[2][0]):
        return board[0][2]

    #board full
    for i in range(0, 3):
        for j in range(0, 3):
            if (board[i][j] == '_'):
                return None

    return 'Tie'   #only possibility

def maximize(alpha,beta): #(-1 loss,1 win,0 tie)
    max_value = -2  
    pos_max_x = None
    pos_max_y = None

    result = finished()
    if result == 'X':
        return (-1,0,0)
    elif result == 'O':
        return (1,0,0)
    elif result == 'Tie':
        return (0,0,0)

    for i in range(0, 3):
        for j in range(0, 3):
            if board[i][j] == '_':
                board[i][j] = 'O'
                (m , min_i , min_j) = minimize(alpha,beta)
                if(m > max_value):
                    max_value = m
                    pos_max_x = i
                    pos_max_y = j
                board[i][j] = '_'
                #alpha-beta
                if(max_value>=beta):
                  return(max_value,pos_max_x,pos_max_y)
                if(max_value>alpha):
                  alpha=max_value
    return (max_value , pos_max_x , pos_max_y)

def minimize(alpha,beta): #(1 loss,-1 win,0 tie)
    min_value = 2
    pos_min_x = None
    pos_min_y = None
    result = finished()
    if result == 'X':
        return (-1,0,0)
    elif result == 'O':
        return (1,0,0)
    elif result == 'Tie':
        return (0,0,0)

    for i in range(0, 3):
        for j in range(0, 3):
            if board[i][j] == '_':
                board[i][j] = 'X'
                (m , max_i , max_j) = maximize(alpha,beta)
                if(m < min_value):
                    min_value = m
                    pos_min_x = i
                    pos_min_y = j
                board[i][j] = '_'
                #alpha-beta
                if(min_value<=alpha):
                  return(min_value,pos_min_x,pos_min_y)
                if(min_value<beta):
                  return(min_value,pos_min_x,pos_min_y)
    return (min_value , pos_min_x , pos_min_y)

class HumanAgent(Agent):
    def __init__(self , aid , computer_agent):
        super().__init__(aid)
        self.computer_agent = computer_agent
    def on_start(self):
        super().on_start()
        self.send_message()
    def react(self , message):
        super().react(message)
        self.send_message()
    def send_message(self):
        try:
            message = ACLMessage(ACLMessage.INFORM)
            message.set_protocol(ACLMessage.FIPA_REQUEST_PROTOCOL)
            message.add_receiver(self.computer_agent)
            self.add_all_agents(message.receivers)
            print("Human's Turn")
            i = None
            j = None
            #check wrong inputs by human
            while (True):
                digit = True
                in_range = True
                new_pos = True
                pos = input('Enter your position:')
                if not pos.isdigit():
                    digit =False
                    print("Please enter a digit!")
                    continue

                pos = int(pos)
                if (pos<1 or pos>9):
                    in_range = False
                    print("Enter between 1-9")
                    continue

            # mapping the position entered with board position
                if(pos<=3):
                    i = 0
                elif (pos>3 and pos<=6):
                    i = 1
                else:
                    i = 2

                if(pos%3 == 0):
                    j = 2
                else:
                    j = pos%3 - 1
                if (board[i][j] != '_'):
                    new_pos =False
                    print("Already occupied!")
                    continue
                break

            board[i][j] = 'X'
            print_board()
            result = finished()

            if(result == 'X'):
                print("You won !")
                sys.exit()
            elif(result =="Tie"):
                print("Tie\n")
                sys.exit()

            message.set_content('Human Agent played "X" at position'+str(pos))
            self.send(message)
        except:
           print("")


    def add_all_agents(self, receivers):
        for receiver in receivers:
            self.agentInstance.table[receiver.localname] = receiver

class ComputerAgent(Agent):
    def __init__(self , aid):
        super().__init__(aid)

    def react(self,message):
        super().react(message)
        self.send_message(AID(message.sender.name))

    def send_message(self, receiver_agent):
        try:
            message = ACLMessage(ACLMessage.INFORM)
            message.set_protocol(ACLMessage.FIPA_REQUEST_PROTOCOL)
            message.add_receiver(receiver_agent)
            self.add_all_agents(message.receivers)
            print("Computer's Turn")

            start = time.time()
            (m, pos_x ,pos_y) = maximize()
            finish = time.time()
            print("time =",round((finish-start),5),"sec")
            board[pos_x][pos_y] = 'O'
            print_board()
            result = finished()
            if(result == 'O'):
                print("Computer won !")
                sys.exit()
            elif(result =="Tie"):
                print("tie")
                sys.exit()

            message.set_content('Computer Agent played "O" at position')
            self.send(message)
        except:
           print("")


    def add_all_agents(self, receivers):
        for receiver in receivers:
            self.agentInstance.table[receiver.localname] = receiver

if __name__ == '__main__':
    agents = list()
    print("TIC TAC TOE")

    print("Possible moves are:- ")
    print(str(1) + '  ' + str(2) + '  ' + str(3))
    print(str(4) + '  ' + str(5) + '  ' + str(6))
    print(str(7) + '  ' + str(8) + '  ' + str(9))
    print_board()
    computer_agent_aid = AID(name = 'Computer Agent')
    computer_agent = ComputerAgent(computer_agent_aid)
    agents.append(computer_agent)
    human_agent = HumanAgent(AID(name = "Human Agent"),computer_agent_aid)
    agents.append(human_agent)
    start_loop(agents)
