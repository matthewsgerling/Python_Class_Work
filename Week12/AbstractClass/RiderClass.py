from abc import ABC, abstractmethod


class Rider(ABC):

    @abstractmethod
    def ride(self):
        raise NotImplementedError("Abstract method not implemented")

    @abstractmethod
    def riders(self):
        raise NotImplementedError("Abstract method not implemented")


class Bicycle(Rider, ABC):
    def __init__(self):
        self.rideType = 'self powered'
        self.num_riders = '1 or 2'

    def ride(self):
        return 'Ride is a ' + self.rideType

    def riders(self):
        return 'Rider can be ' + self.num_riders

    def __str__(self):
        return str(self.ride()) + str(self.riders())


class MoterCycle(Rider, ABC):
    def __init__(self):
        self.rideType = 'Engine'
        self.num_riders = '1 or 2'

    def ride(self):
        return 'Ride is a ' + self.rideType

    def riders(self):
        return 'Rider can be ' + self.num_riders

    def __str__(self):
        return str(self.ride()) + str(self.riders())


class Car(Rider, ABC):
    def __init__(self):
        self.rideType = 'Engine'
        self.num_riders = '1 or more'

    def ride(self):
        return 'Ride is a ' + self.rideType

    def riders(self):
        return 'Rider can be ' + self.num_riders

    def __str__(self):
        return str(self.ride()) + str(self.riders())


car = Car()
Bike = Bicycle()
motorBike = MoterCycle()
print(str(car))
print(str(Bike))
print(str(motorBike))
