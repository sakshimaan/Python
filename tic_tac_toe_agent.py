from pade.misc.utility import display_message, start_loop
from pade.core.agent import Agent
from pade.acl.aid import AID
from pade.acl.messages import ACLMessage
import json


def printBoard(board):
    print("\n\n")
    t=1
    for i in range(9):
        if board[i]!=-1:
            print(board[i], end="")
        else:
            print(i+1, end="")
        if t!=3:
            print(" | ",end ="")
        if t>=3:
            t=0
            print("\n",end="")
        t+=1
    print("\n\n")

#check if the player is the winner or not
def playerWon(magicSquare, board, player):
    for i in range(0,9):
        for j in range(0,9):
            for k in range(0,9):
                if (i != j and i != k and j != k):
                    if (board[i] == player and board[j] == player and board[k] == player):
                        if (magicSquare[i] + magicSquare[j] + magicSquare[k] == 15):
                            return True
    return False

#check winner is it human or computer
def checkWinner(magicSquare, board):
    if playerWon(magicSquare, board, 'x'):
        print("x win!")
    elif playerWon(magicSquare, board, 'o'):
        print("o win!")
    else:
        print("No winner yet...")


def canWin(magicSquare, board, player):
    for i in range(0,9):
        for j in range(0,9):
            for k in range(0,9):
                if (i != j and i != k and j != k):
                    if (board[i] == player and board[j] == player and board[k] == -1):########################
                        if (magicSquare[i] + magicSquare[j] + magicSquare[k] == 15):
                            return k+1
    return -1

def possWin(magicSquare, board, player):
    cWin = canWin(magicSquare, board, player)
    if cWin==-1:
        return -1
    else:
        return cWin

def go(board, move, num):
    if move%2==0:
        board[num-1] = 'o'
    else:
        board[num-1] = 'x'

def make2(magicSquare, board, player):
    if board[5-1]==-1:
        return 5
    for i in range(0,9):
        for j in range(0,9):
            for k in range(0,9):
                if (i != j and i != k and j != k):
                    if (board[i] == player and board[j] == -1 and board[k] == -1):########################
                        if (magicSquare[i] + magicSquare[j] + magicSquare[k] == 15):
                            if j==(2-1) or j==(4-1) or j==(6-1) or j==(8-1):
                                return j+1
    return -1

def findBlank(board):
    for i in range(0,9):
        if board[i]==-1:
            return i

def computerMove(magicSquare, board, move):
    if move==1:
        go(board,move,1)
    elif move==2:
        if board[5-1]==-1:
            go(board,move,5)
        else:
            go(board,move,1)
    elif move==3:
        if board[9-1]==-1:
            go(board,move,9)
        else:
            go(board,move,3)
    elif move==4:
        p = possWin(magicSquare, board,'x')
        if p==-1:
            mak2 = make2(magicSquare, board, 'o')
            go(board,move,mak2)
        else:
            go(board,move,p)
    elif move==5:
        px = possWin(magicSquare, board,'x')
        po = possWin(magicSquare, board,'o')
        if px>=0:
            go(board,move,px)
        elif po>=0:
            go(board,move,po)
        elif board[7-1]==-1:
            go(board,move,7)
        else:
            go(board,move,3)
    elif move==6:
        px = possWin(magicSquare, board,'x')
        po = possWin(magicSquare, board,'o')
        if po>=0:
            go(board,move,po)
        elif px>=0:
            go(board,move,px)
        else:
            mak2 = make2(magicSquare, board, 'o')
            go(board,move,mak2)
    elif move==7:
        px = possWin(magicSquare, board,'x')
        po = possWin(magicSquare, board,'o')
        if px>=0:
            go(board,move,px)
        elif po>=0:
            go(board,move,po)
        else:
            blank = findBlank(board)
            go(board,move,blank)
    elif move==8:
        px = possWin(magicSquare, board,'x')
        po = possWin(magicSquare, board,'o')
        if po>=0:
            go(board,move,po)
        elif px>=0:
            go(board,move,px)
        else:
            blank = findBlank(board)
            go(board,move,blank)
    elif move==9:
        px = possWin(magicSquare, board,'x')
        po = possWin(magicSquare, board,'o')
        if px>=0:
            go(board,move,px)
        elif po>=0:
            go(board,move,po)
        else:
            blank = findBlank(board)
            go(board,move,blank)

def Value(board, move):
    print("\n\n This is your turn : ")
    printBoard(board)
    while True:
        n = int(input("Enter the number: "))
        if board[n-1]==-1:
            board[n-1] = 'x'
            break
        else:
            print("Please enter correct input :- \n\n")

    printBoard(board)



class HumanAgent(Agent):
    def __init__(self, aid, receiver_agent, message):
        super().__init__(aid)
        self.receiver_agent = receiver_agent
        self.message = message
        

    def react(self, message):
        super().react(message)
        msg = message.content
        Value(msg['board'],msg['move'])
        msg['move'] = msg['move'] + 1
        if playerWon(msg['magicSquare'], msg['board'], 'x'):
            print("\tYaay!!!.....You won the game")
            print("END")
        elif msg['mov']==9:
            print("GAME TIES")
        else:
            self.message = msg
            self.send_message()

    def on_start(self):
        super().on_start()
        Value(self.message['board'], self.message['move'])
        msg['move'] = msg['move'] + 1
        self.send_message()

    def send_message(self):
        message = ACLMessage(ACLMessage.INFORM)
        message.set_protocol(ACLMessage.FIPA_REQUEST_PROTOCOL)
        message.add_receiver(self.receiver_agent)
        self.add_all_agents(message.receivers)
        message.set_content(self.message)
        self.send(message)

    def add_all_agents(self, receivers):
        for receiver in receivers:
            self.agentInstance.table[receiver.localname] = receiver

class ComputerAgent(Agent):
    def __init__(self, aid):
        super().__init__(aid)

    def react(self, message):
        super().react(message)
        print("\n\ncomputer turn :- ")
        msg= message.content
        computerMove(msg['magicSquare'], msg['board'], msg['move'])
        msg['move'] = msg['move'] + 1

        printBoard(msg['board'])
        
        if playerWon(msg['magicSquare'], msg['board'], 'o'):
            print("\nThis time computer won....\n")
            print("End")
        elif msg['mov']==9:
            print("GAME TIES")
        else:
            self.message = msg
            self.send_message(message.sender.name)

    def send_message(self, receiver_agent):
        message = ACLMessage(ACLMessage.INFORM)
        message.set_protocol(ACLMessage.FIPA_REQUEST_PROTOCOL)
        message.add_receiver(receiver_agent)
        self.add_all_agents(message.receivers)
        message.set_content(self.message)
        self.send(message)

    def add_all_agents(self, receivers):
        for receiver in receivers:
            self.agentInstance.table[receiver.localname] = receiver

if __name__ == '__main__':
    msg = {'board':[-1,-1,-1,-1,-1,-1,-1,-1,-1], 'magicSquare':[8,3,4,1,5,9,6,7,2], 'move':1}
    
    agents = list()
    computer_agent_aid = AID(name='receiver@localhost:{}'.format(30001))
    computerAgent = ComputerAgent(computer_agent_aid)
    agents.append(computerAgent)
    
    human_agent = HumanAgent(AID(name='sender@localhost:{}'.format(30000)), computer_agent_aid, msg)
    agents.append(human_agent)

    start_loop(agents)
