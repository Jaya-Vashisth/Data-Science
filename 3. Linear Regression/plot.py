import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D

a = np.array([1,2,3])
b = np.array([4,5,6,7])

# fucntion create matric and give coordinates 
a,b = np.meshgrid(a,b)
print(a)
print(b)

#3d plot example
fig = plt.figure()
axes = fig.add_subplot(projection = '3d')
axes.plot_surface(a, b, a**2+b**2 , cmap = 'rainbow')
plt.show()




a = np.arange(-1,1,0.02)
b = a
a, b = np.meshgrid(a,b)


# surface plot
fig = plt.figure()
axes = fig.add_subplot(projection = '3d')
axes.plot_surface(a, b, a**2+b**2 , cmap = 'rainbow')
plt.show()

# contour plot
fig = plt.figure()
axes = fig.add_subplot(projection = '3d')
axes.contour(a,b,a**2 + b**2 , cmap = 'rainbow')
plt.title('contourplot')
plt.show()
