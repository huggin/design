from abc import ABCMeta, abstractmethod


class VehicleSize:
    MOTORCYCLE = 1
    COMPACT = 1
    LARGE = 5


class Vehicle(metaclass=ABCMeta):
    def __init__(self, vehicle_size, license_plate):
        self.sz = vehicle_size
        self.license_plate = license_plate
        self.spot = None

    def size(self):
        return self.sz

    def leave(self):
        self.spot.finish()

    def park(self, spot):
        self.spot = spot
        self.spot.occupy(self)


class Motocycle(Vehicle):
    def __init__(self, license_plate):
        super().__init__(VehicleSize.MOTORCYCLE, license_plate)


class Car(Vehicle):
    def __init__(self, license_plate):
        super().__init__(VehicleSize.COMPACT, license_plate)


class Bus(Vehicle):
    def __init__(self, license_plate):
        super().__init__(VehicleSize.LARGE, license_plate)


class ParkingLot(object):
    def __init__(self, num_floor):
        self.num_floor = num_floor
        self.floors = []
        for i in range(num_floor):
            self.floors.append(Floor(self, i))

    def find_spot(self, vehicle):
        for floor in self.floors:
            spot = floor.find_available(vehicle.size())
            if spot:
                return spot

        return None


class Floor(object):
    ROW = 10
    COL = 10

    def __init__(self, lot, floor):
        self.parking_lot = lot
        self.floor = floor
        self.parking_spots = [[0 for _ in range(self.COL)] for _ in range(self.ROW)]

    def find_available(self, sz):
        for i in range(self.ROW):
            for j in range(self.COL):
                if sz == 1:
                    if self.parking_spots[i][j] == 0:
                        return ParkingSpot(self, i, j, sz)
                else:  # sz == 5
                    if (
                        j + 5 >= self.COL
                        or self.parking_spots[i][j]
                        or self.parking_spots[i][j + 1]
                        or self.parking_spots[i][j + 2]
                        or self.parking_spots[i][j + 3]
                        or self.parking_spots[i][j + 4]
                    ):
                        continue
                    return ParkingSpot(self, i, j, sz)

        return None

    def finish(self, spot):
        for i in range(spot.spot_number, spot.spot_number + spot.spot_size):
            self.parking_spots[spot.row][i] = 0

    def occupy(self, spot):
        for i in range(spot.spot_number, spot.spot_number + spot.spot_size):
            self.parking_spots[spot.row][i] = 1


class ParkingSpot(object):
    def __init__(self, floor, row, spot_number, spot_size):
        self.floor = floor
        self.row = row
        self.spot_number = spot_number
        self.spot_size = spot_size
        self.vehicle = None

    def is_available(self):
        return self.vehicle is None

    def occupy(self, vehicle):
        self.vehicle = vehicle
        self.floor.occupy(self)

    def finish(self):
        self.floor.finish(self)
