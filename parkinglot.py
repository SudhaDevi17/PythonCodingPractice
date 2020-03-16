
class car:
    def __init__(self, val):
        self.carsize = val
class ParkingLot:
    def __init__(self):
        self.carlane = []
        self.bikelane = []

    def parkvehicle( self, car):
        self.carlane.append(car)
    def removevehicle(self, location):
        self.carlane.pop(location)
if __name__ == "__main__":
    p = ParkingLot()
    redcar = car('big')
    p.parkvehicle(redcar)
    location=0
    p.removevehicle(location)




