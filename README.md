# Kandilli API
[![Latest Version](https://pypip.in/version/kandilli/badge.svg)](https://pypi.python.org/pypi/kandilli/)
[![Downloads](https://pypip.in/download/kandilli/badge.svg)](https://pypi.python.org/pypi/kandilli/)
[![Download format](https://pypip.in/format/kandilli/badge.svg)](https://pypi.python.org/pypi/kandilli/)
[![Supported Python versions](https://pypip.in/py_versions/kandilli/badge.svg)](https://pypi.python.org/pypi/kandilli/)
[![License](https://pypip.in/license/kandilli/badge.svg)](https://pypi.python.org/pypi/kandilli/)

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
