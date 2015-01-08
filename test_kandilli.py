import unittest
import datetime
import random
from api import LastEarthquakes
from itertools import islice


class ApiTest(unittest.TestCase):
    def setUp(self):
        self.many = 10
        self.api = LastEarthquakes(self.many)

    def test_return_iterator_data(self):
        for d in islice(self.api, self.many):
            self.assertIsInstance(d, dict)

    def test_return_zero_data_length(self):
        self.assertEqual(len(self.api), 0)

    def test_return_data_length(self):
        self.api.refresh()
        self.assertEqual(self.many, len(self.api))

    def test_return_too_many_items(self):
        too_many_items = LastEarthquakes(5000)
        self.assertNotEqual(5000, len(too_many_items))

    def test_return_dict_items(self):
        self.assertIsInstance(self.api.data, list)

    def test_many_getter(self):
        self.api.many = 4
        self.assertEqual(4, self.api.many)

    def test_refresh(self):
        self.api.many = 2
        self.api.refresh()
        self.assertEqual(2, len(self.api))

    def test_cache(self):
        x = self.api.data
        y = self.api.data
        self.assertEqual(x, y)

    def test_maxlen(self):
        self.api.refresh()
        self.assertGreater(self.api.maxlen, 500)

    def test_maxlen_zero(self):
        self.assertEqual(self.api.maxlen, 0)

    def test_time_format_time(self):
        test_data = self.api.data[random.randrange(0, len(self.api))]["tarih"]
        datetime_obj = datetime.datetime.strptime(test_data, "%Y.%m.%d")
        self.assertIsInstance(datetime_obj, datetime.date)

    def test_time_format_hour(self):
        test_data = self.api.data[random.randrange(0, len(self.api))]["saat"]
        datetime_obj = datetime.datetime.strptime(test_data, "%H:%M:%S")
        self.assertIsInstance(datetime_obj, datetime.date)
