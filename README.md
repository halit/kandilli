# Kandilli API

Simple kandilli last earthquakes api.

# Installation

    pip install kandilli

# Usage

    from kandilli import LastEarthquakes
    from itertools import islice
    
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
