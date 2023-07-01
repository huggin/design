import unittest
from parking_lot import *


class ParkingLotTest(unittest.TestCase):
    def test_motocycle(self):
        moto = Motocycle("ABC123")
        self.assertEqual(moto.size(), 1)
    
    def test_park(self):
        lot = ParkingLot(5)
        v = Car("BCD456")
        spot = lot.find_spot(v)
        self.assertIsNotNone(spot)
        v.park(spot)
        v2 = Bus("FGH789")
        spot = lot.find_spot(v2)
        self.assertIsNotNone(spot)
        self.assertEqual(spot.floor.floor, 0)
        self.assertEqual(spot.row, 0)
        self.assertEqual(spot.spot_number, 1)
        
        v.leave()

        v3 = Motocycle("ABC123")
        spot3 = lot.find_spot(v3)
        self.assertIsNotNone(spot3)
        self.assertEqual(spot3.floor.floor, 0)
        self.assertEqual(spot3.row, 0)
        self.assertEqual(spot3.spot_number, 0)

        

if __name__ == '__main__':
    unittest.main()
