"""
Last Earthquakes Api
"""
import urllib
from pyquery import PyQuery

__version__ = '0.1.0'
__all__ = ['LastEarthquakes']

DEFAULT_MANY = 10
QUERY_URL = "http://www.koeri.boun.edu.tr/scripts/lst6.asp"
COL_NAMES = ('tarih', 'saat', 'enlem', 'boylam', 
             'derinlik', 'md', 'ml', 'mw', 'yer', 'nitelik')


class ApiError(Exception):
    """
    ApiError exception class
    """
    def __init__(self, name):
        """
        Default constructor for exception class
        :param name: str
        """
        self.name = name

    def __repr__(self):
        return "<ApiError {}>".format(self.name)


class LastEarthquakes(object):
    """
    Last earthquakes api.
    """
    def __init__(self, many=DEFAULT_MANY):
        """
        Api constructor method
        :param many: integer
        """
        self.__features = dict(data_start=6, html_tag='pre',
                               html_del='\r', many=many)
        self.__cache = None
        self.__data = None

    def __request(self):
        """
        Request url and return all html content
        """
        try:
            data = urllib.urlopen(QUERY_URL).read()
        except IOError:
            raise ApiError("Connection error!")

        return data

    def __parse(self, content):
        """
        Parse html content and return raw data
        :param content: string
        """
        parser = PyQuery(content)
        temp_data = parser(self.__features.get("html_tag")).text()

        return temp_data.split(self.__features.get("html_del"))

    def __iter__(self):
        """
        Iterator for data
        """
        self.__data = self.__parse(self.__request())

        start = self.__features.get("data_start")
        many = self.__features.get("many")
        finish = many + start if len(self.__data) > many else len(self.__data)
        for i in xrange(start, finish):
            datum = self.__data[i].split()
            datum[8:-1] = [" ".join(datum[8:-1])]

            yield dict(zip(COL_NAMES, datum))

    def __len__(self):
        """
        Data length descriptor
        """
        return 0 if not self.__data else len(self.__cache)

    def __repr__(self):
        """
        Repr descriptor for instances
        """
        return "<{name} many={many}>".format(name="LastEarthquakesApi",
                                             many=self.__features.get("many"))

    def __str__(self):
        """
        String descriptor for instances
        """
        return self.__repr__()

    @property
    def data(self):
        """
        Property method for data
        """
        if not self.__data:
            self.__cache = list(self)
            return self.__cache
        else:
            return self.__cache

    @property
    def many(self):
        """
        Getter method for many variable
        """
        return self.__features.get("many")

    @many.setter
    def many(self, value):
        """
        Setter method for many variable
        :param value: int
        """
        if not self.__data:
            new_many = value if DEFAULT_MANY > value else DEFAULT_MANY
        else:
            new_many = min(value, len(self.__data))
        self.__features["many"] = new_many

    @property
    def maxlen(self):
        """
        Getter method for max length
        """
        offset = self.__features.get("data_start")
        return 0 if not self.__data else len(self.__data) - offset

    def refresh(self):
        """
        Refresh method for re-check all data
        """
        self.__cache = list(self)