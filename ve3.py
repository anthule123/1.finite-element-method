# %%
import matplotlib.pyplot as plt
import numpy as np
from mpl_toolkits.mplot3d import Axes3D
M=32
x = np.outer(np.linspace(0,1, M), np.ones(M))
y = x.copy().T # transpose
z = np.zeros((M,M))
for i in range(0,M):
    for j in range(0,M):
        if(i + j <=M):
            z[i][j] = -1
fig = plt.figure(figsize =(14, 9))
ax = plt.axes(projection ='3d')
 
# Creating plot
ax.plot_surface(x, y, z,color = 'green')
 
# show plot
plt.show()

