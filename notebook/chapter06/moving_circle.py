import matplotlib.pyplot as plt
import matplotlib.animation as animation
import numpy as np

dt = 0.01
fig = plt.figure()
ims = []

for i in range(int(1/dt)):
	t = dt*i
	
	x = np.cos(t*2*np.pi)
	y = np.sin(t*2*np.pi)
	im = plt.plot(x,y,color='b', marker='o', markersize=20)
	ims.append(im)

ani = animation.ArtistAnimation(fig,ims)
plt.show()