import unittest
from bus_reservation import calculate_fare, check_availability


class TestBusReservation(unittest.TestCase):

    def test_calculate_fare(self):
        self.assertEqual(calculate_fare(2, 500), 1000)

    def test_check_availability(self):
        self.assertEqual(check_availability(50, 20), 30)

    def test_no_available_seats(self):
        self.assertEqual(check_availability(50, 50), 0)


if __name__ == '__main__':
    unittest.main()