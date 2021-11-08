import random
board = [' ' for x in range(10)]

def insertMove(symbol, pos):
    board[pos]=symbol

def isFree(pos):
    return board[pos]==' '

def printBoard(board):
    print("/---|---|---\\")   
    print("| " + board[1] + " | " + board[2] + " | " + board[3] + " |") 
    print("|-----------|")  
    print("| " + board[4] + " | " + board[5] + " | " + board[6] + " |") 
    print("|-----------|")   
    print("| " + board[7] + " | " + board[8] + " | " + board[9] + " |") 
    print("/---|---|---\\")

def boardIsFull(board):
    if board.count(' ')>0:
        return False
    else:
        return True

def isWinner(b,s):
    return ((b[1] == s and b[2] == s and b[3] == s) or
    (b[4] == s and b[5] == s and b[6] == s) or
    (b[7] == s and b[8] == s and b[9] == s) or
    (b[1] == s and b[4] == s and b[7] == s) or
    (b[2] == s and b[5] == s and b[8] == s) or
    (b[3] == s and b[6] == s and b[9] == s) or
    (b[1] == s and b[5] == s and b[9] == s) or
    (b[3] == s and b[5] == s and b[7] == s))

def playerMove():
    run=True
    while run:
        move=input("Enter the position (1-9) to place 'X': ")
        try:
            move=int(move)
            if move in range(1,10):
                if isFree(move):
                    run = False
                    insertMove('X',move)
                else:
                    print("Sorry, the place is occupied")
            else:
                print("Please enter a number between 1 to 9")
        except:
            print("Please enter a number")

def computerMove():
    possibleMoves=[x for x,symbol in enumerate(board) if symbol==' ' and x!=0]
    move=0
    for symbol in ['O', 'X']:
        for i in possibleMoves:
            copyboard=board[:]
            copyboard[i]=symbol
            if isWinner(copyboard, symbol):
                move=i
                return move

    cornersOpen=[]
    for i in possibleMoves:
        if i in [1,3,7,9]:
            cornersOpen.append(i)

    if len(cornersOpen)>0:
        move = random.choice(cornersOpen)
        return move

    if 5 in possibleMoves:
        move=5
        return move

    edgesOpen=[]
    for i in possibleMoves:
        if i in [2,4,6,8]:
            edgesOpen.append(i)
    
    if len(edgesOpen)>0:
        move = random.choice(edgesOpen)
        return move




def main():
    print("Welcome to TicTacToe")
    printBoard(board)
    while not(boardIsFull(board)):
        if not(isWinner(board , 'O')):
            playerMove()
            printBoard(board)
        else:
            print("sorry you loose!")
            break

        if not(isWinner(board , 'X')):
            move = computerMove()
            if move == None:
                print("Tie game")
                break
            else:
                insertMove('O' , move)
                print("computer placed an 'O' in position" , move , ':')
                printBoard(board)
        else:
            print("Congratulations!! You win!")
            break
        

while True:
    x = input("Do you want to play? (y/n)")
    if x.lower() == 'y':
        board = [' ' for x in range(10)]
        print('--------------------')
        main()
    else:
        break


    



		