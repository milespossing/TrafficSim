import trafficsimcore.car
import roaddensity.roadDensity
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
import numpy as np

if __name__ == '__main__':
    for i in range(0,100):
        trafficsimcore.cars.append(trafficsimcore.car.RegularDriver(5*i))
    trafficsimcore.initialize()
    positions = []
    for i in range(0,400):
        trafficsimcore.log()
        trafficsimcore.iterate(1)
    [time,density] = roaddensity.roadDensity.calculate(trafficsimcore.locations,400)
    array = np.array(density)
    hf = plt.figure()
    ha = hf.add_subplot(111, projection='3d')
    x = range(len(density))
    y = range(len(density[0]))
    X, Y = np.meshgrid(x, y)
    ha.plot_surface(X,Y,array)
    plt.show()