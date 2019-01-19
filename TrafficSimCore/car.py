import trafficsimcore.utilities

class Car():
    def __init__(self,location=0.0):
        self.location = location
        self.speed = 0.0




class RegularDriver(Car):
    def __init__(self,location=0.0):
        super().__init__(location)
        self.minimumDistance = 10.0
        self.maxSpeed = 31
        self.accelerationRate = 10.0
        self.decelerationRate = 20.0
        self.nextCar = None

    @property
    def maxSpeedKph(self):
        return self.maxSpeed * 36 #speed in m/s rather than km/h

    @maxSpeedKph.setter
    def maxSpeedKph(self,value):
        self.maxSpeed = value / 36

    def iterate(self,period):
        if trafficsimcore.utilities.carDistance(self,self.nextCar) > self.minimumDistance:
            if self.speed < self.maxSpeed:
                self.speed += self.accelerationRate * period
        else:
            if self.speed > self.nextCar.speed:
                self.speed -= self.decelerationRate * period
        self.location += self.speed
