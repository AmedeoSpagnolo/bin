import matplotlib.pyplot as plt
import random

X = []
Y = []
X1 = []
Y1 = []
for x in range(300):
  X.append(random.randint(0,100))
  Y.append(random.randint(0,100))

for x in range(30):
    X1.append(random.randint(0,100))
    Y1.append(random.randint(0,100))

plt.plot(X,Y,color='green',marker='o',markersize=6,linestyle='None', markeredgecolor='None')
plt.plot(X1,Y1,color='red',marker='o',markersize=6,linestyle='None', markeredgecolor='None')
plt.axis([0, 100, 0, 100])
plt.show()
