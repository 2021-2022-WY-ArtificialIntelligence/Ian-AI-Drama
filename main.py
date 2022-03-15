
from TicTacToe import *
from TicTacToeData import *
from NeuralNetwork import *
import numpy as np

from dense import Dense
from activations import Sigmoid, Softmax, Tanh
from losses import mse, mse_prime
from network import predict, train


manualTrain(40)


# X = matrixizer("memory.pickle")
# Y = matrixizer("trainingData.pickle")

# network = [
#     Dense(9, 7),
#     Tanh(),
#     Dense(7, 7),
#     Sigmoid(),
#     Dense(7, 7),
#     Sigmoid(),
#     Dense(7, 9),
#     Tanh(),
# ]


# testBoard = [[ "X" , "_" , "X" ],
#              [ "X" , "_" , "_" ],
#              [ "O" , "_" , "O" ] ]

# testGame = GameState(testBoard, 1)
# testArray = testGame.makeArray()

# train(network, mse, mse_prime, X, Y, epochs=10000, learning_rate=0.1)
# z = predict(network,  testArray)

def solver(network, testArray):
    z = predict(network,  testArray)

    listOfPossiblePlaces = [i[0] for i in z]
    print(listOfPossiblePlaces)
    print(np.argmax(listOfPossiblePlaces) + 1)

# solver(network, testArray)
    


