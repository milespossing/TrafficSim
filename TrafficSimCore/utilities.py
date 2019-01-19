import math

def carDistance(car1,car2):
    if car1 is None or car2 is None:
        return math.inf
    return abs(car1.location - car2.location)
