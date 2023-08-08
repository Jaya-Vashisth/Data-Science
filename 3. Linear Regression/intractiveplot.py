import matplotlib.pyplot as plt
import numpy as np
import pandas as pd


X = pd.read_csv('dataset/Linear_X_Train.csv').values
Y = pd.read_csv('dataset/Linear_Y_Train.csv').values



theta = np.load("thetalist.npy")
#100,2

t0 = theta[:,0]
t1 = theta[:,1]
plt.ion()

for i in range(0,50,3):
    y_ = t1[i]*X + t0

    #point of training data
    plt.scatter(X,Y)
    #prediction line
    plt.plot(X,y_)

    plt.draw()
    plt.pause(1)
    plt.clf()

