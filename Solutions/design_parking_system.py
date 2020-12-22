class ParkingSystem(object):

    def __init__(self, big, medium, small):
        """
        :type big: int
        :type medium: int
        :type small: int
        """
        self.lot = {
            1: [big,0],
            2: [medium,0],
            3: [small,0]
        }

    def addCar(self, carType):
        """
        :type carType: int
        :rtype: bool
        """
        if self.lot[carType][1] < self.lot[carType][0]:
            self.lot[carType][1] += 1
            return True
        else:
            return False