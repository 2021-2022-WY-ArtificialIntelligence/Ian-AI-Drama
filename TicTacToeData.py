from TicTacToe import *
import pickle
import numpy as np
import os

def ifPickleEmpty():
  pickle_set = open("memory.pickle" , "wb")
  pickle.dump([GameState()], pickle_set)
  pickle_set.close()

def printMemory(file):
  pickle_in = open(file , "rb")
  mem = pickle.load(pickle_in)
  for i in mem:
    print(f"PLAYER = {i.player}")
    i.display()

def detectFileEmpty(fileName):
  filesize = os.path.getsize(fileName)
  if filesize == 0:
    ifPickleEmpty()

def clearFile(fileName):
  file = open(fileName , "w")
  file.truncate()
  file.close()

def listOfRandomGames(numberOfGames):
    pickle_in = open("memory.pickle" , "wb")
    listOfGamestates = []

    for i in range(numberOfGames):
        listOfGamestates.append(randomBoard())

    pickle.dump(listOfGamestates, pickle_in)
    pickle_in.close()


def inputToArray(x):
  # takes in a human input from 1 - 9 and uses that to make a matrix of 
  # zeros except where the number is placed
  blankList = [0 for i in range(9)]
  blankList[x - 1] = "1"
  return blankList

  
def painfulHumanTraining():
    pickle_out = open("memory.pickle" , "rb")
    listOfGames = pickle.load(pickle_out)
    pickle_train_data = open("trainingData.pickle", "wb")
    listOfTrainingData = []
    for i in listOfGames:
        i.display()
        x = int(input())
        listOfTrainingData.append(inputToArray(x))
        print("++++++++++++++++++")
    print("YOU ARE DONE, CONGRATS")
    pickle.dump(listOfTrainingData, pickle_train_data)
    pickle_out.close()
    pickle_train_data.close()


def matrixizer(file): # takes in either the training data file 
                      # or the memory and makes the boards into 
                      # matricies to be read by the neural network
    pickle_in = open(file , "rb")
    listOfGamestates = pickle.load(pickle_in)

    listOfBoardArrays = []

    for i in listOfGamestates:
        listOfBoardArrays.append(i.makeArray())
    lengthOfArray = len(listOfBoardArrays)
        
    matrixed = np.reshape(listOfBoardArrays, (lengthOfArray, 9, 1))   
    return matrixed

def manualTrain(games):
  clearFile("memory.pickle")
  clearFile("trainingData.pickle")
  listOfRandomGames(games)
  painfulHumanTraining()

