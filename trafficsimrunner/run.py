import trafficsimcore.car
import matplotlib.pyplot as plt

if __name__ == '__main__':
    car = trafficsimcore.car.RegularDriver()
    car2 = trafficsimcore.car.RegularDriver()
    car2.location = 5
    car2.maxSpeedKph = 100
    trafficsimcore.cars.append(car)
    trafficsimcore.cars.append(car2)
    trafficsimcore.initialize()
    positions = []
    for i in range(0,100):
        trafficsimcore.log()
        trafficsimcore.iterate(1)
    plt.plot(trafficsimcore.locations)
    plt.ylabel('location')
    plt.show()