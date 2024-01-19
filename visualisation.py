import matplotlib.pyplot as plt
import knearest as knn
import dataConstruction as dcstn 



#data = dcstn.rings(100)
data = dcstn.spots(100)



xr = []
yr = []

for point in data:
    plt.plot(point.x_pos,point.y_pos,point.label,markersize=1)

plt.axis([0,50,0,50])
plt.show()