import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
import numpy as np
import pandas as pd


X = pd.read_csv('dataset/Linear_X_Train.csv').values
Y = pd.read_csv('dataset/Linear_Y_Train.csv').values



theta = np.load("thetalist.npy")
J = np.load('J.npy')
loss_list = np.load('losslist.npy')


t0 = theta[:,0]
t1 = theta[:,1]
plt.ion()


fig = plt.figure()
axes = fig.add_subplot(projection = '3d')
axes.plot_surface(t0, t1,J, cmap = 'rainbow')

for i in range(100):
   
    axes.scatter(t0,t1, loss_list[i])

    plt.draw()
    plt.pause(1)
    plt.clf()
