# Kandilli API
[![Latest Version](https://img.shields.io/pypi/v/kandilli.svg)](https://pypi.python.org/pypi/kandilli/)
[![Downloads](https://img.shields.io/pypi/dm/kandilli.svg)](https://pypi.python.org/pypi/kandilli/)
[![Download format](https://img.shields.io/pypi/format/kandilli.svg)](https://pypi.python.org/pypi/kandilli/)
[![Supported Python versions](https://img.shields.io/pypi/pyversions/kandilli.svg)](https://pypi.python.org/pypi/kandilli/)
[![License](https://img.shields.io/pypi/l/kandilli.svg)](https://pypi.python.org/pypi/kandilli/)
[![Build Status](https://api.travis-ci.org/halitalptekin/kandilli.png)](https://travis-ci.org/halitalptekin/kandilli)

Simple kandilli last earthquakes api.

# Installation

    pip install kandilli

# Usage

    from kandilli import LastEarthquakes
    
    api = LastEarthquakes(10)
    print api.data[0]
    
    api.refresh()
    print api.data[0]
    
    api.many = 25
    api.refresh()
    print api.data[0]
    
    api.many = 250
    for data in api:
        print data['yer']
