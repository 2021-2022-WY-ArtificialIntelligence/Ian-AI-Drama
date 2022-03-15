import pickle
import copy
import random
import numpy as np
import math




class GameState:
  # GameState is the class that will represent the state of the board and the current player
   
    def __init__(self, *args):
        

        if len(args) == 0:
            self.board = [ [ "_" , "_" , "_" ] ,
                       [ "_" , "_" , "_" ] ,
                       [ "_" , "_" , "_" ] ]

            self.player = -1
        else:
            self.board = args[0]
            self.player = args[0]

    def setPlayer(self, player):
        self.player = player
    
    def setBoard(self, board):
        self.board = board

    def display(self):
        for i in self.board:
            print(i)

    def placeToCoord(self, x):
        rowLen = len(self.board[0])
        return ( int ( ( x - 1 ) / rowLen ) , ( x - 1 ) % rowLen )
    
    def changePlayer(self):
        if self.player == 1:
            self.player = -1
            return -1
        else:
            self.player = 1
            return 1

    def setPlace(self, place, player):
        if player == 1:
            char = "O"
        else:
            char = "X"
        
        boardCopy = self.board
        coord = self.placeToCoord(place)

        current = self.board[coord[0]][coord[1]]

        if current == "_":
            boardCopy[coord[0]][coord[1]] = char
            return GameState(boardCopy , self.changePlayer())
        else:
            print("CANNOT MOVE THERE") # If the selected spot already has a piece the player's turn is not ended
            return GameState(boardCopy , player)

    def checkRow(self, row):
        first = row[0]
        ans = False
        for i in row:
            if i == first and i != "_":
                ans = True
            else:
                ans = False
                break
        if ans:
            return row[0]
        else:
            return None

    def checkRows(self):
  
     for i in self.board:
        if self.checkRow(i):
            return self.checkRow(i)
        return False

    def checkCols(self):
        for i in range(len(self.board[0])):
            col = []
            for k in self.board:
                col.append(k[i])
            if self.checkRow(col):
                return self.checkRow(col)
    
    def checkDiagnols(self):
        board = self.board
        diagnol1 = []
        diagnol2 = [board[0][2] , board[1][1] , board[2][0]]
        
        for i in range(len(board)):
            diagnol1.append(board[i][i])

        if self.checkRow(diagnol1):
            return self.checkRow(diagnol1)
        elif self.checkRow(diagnol2):
            return self.checkRow(diagnol2)
        else:
            return False

    def humanInput(self):
        x = int(input())
        newState = copy.deepcopy(self.setPlace( x, self.player))
        self.player = self.changePlayer()
        newState.player = self.changePlayer()
        return newState

    def randomPlay(self):
        listOfAvailable = []

        for i in range(len(self.board)):
            for k in range(len(self.board[i])):
                if self.board[i][k] == "_":
                    rowLen = len(self.board[0])
                    place = ( i * rowLen + k ) + 1
                    listOfAvailable.append(place)
        randomPlace = int(random.random() * len(listOfAvailable))
        place = listOfAvailable[randomPlace]

        newState = copy.deepcopy(self.setPlace(place, self.player))
        self.changePlayer()
        newState.player = self.changePlayer()
        return newState


    def isFull(self):
        board = self.board
        for i in board:
            for k in i:
                if k == "_":
                    return False
            
        return True

    def isEnd(self):
        if self.checkRows():
            return False
        elif self.checkCols():
            return False
        elif self.checkDiagnols():
            return False
        elif self.isFull():
            return False
        else:
            return True
    
    def makeArray(self):
        arrayOfBoard = []
        for i in self.board:
            for k in i:
                if k == "_":
                    arrayOfBoard.append(0)
                elif k == "O":
                    arrayOfBoard.append(1)
                else:
                    arrayOfBoard.append(-1)
        return arrayOfBoard

def randomBoard():
    game = GameState()
    randomNumberOfPlays = (int(random.random() * 4) + 1) * 2
    print(randomNumberOfPlays)
    pastState = copy.deepcopy(game)
    while game.isEnd() and randomNumberOfPlays != 0:
        randomNumberOfPlays -= 1
        pastState = copy.deepcopy(game)
        game.randomPlay()
    return pastState
