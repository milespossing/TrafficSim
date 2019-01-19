cars = []
locations = []

def log():
    output = []
    for car in cars:
        output.append(car.location)
    locations.append(output)

def iterate(period):
    for car in cars:
        car.iterate(period)

def initialize():
    cars.sort(key=lambda c: c.location)
    for i in range(0,len(cars) - 1):
        cars[i].nextCar = cars[i + 1]
