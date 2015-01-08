try:
    from setuptools import setup
except ImportError:
    from distutils.core import setup

config = dict(description='Kandilli last earthquakes api',
            long_description=open('README.md').read(),
            author='Halit Alptekin',
            url='https://github.com/halitalptekin/kandilli', 
            author_email='info@halitalptekin.com', 
            license='MIT',
            keywords='api, earthqueke, earthquakes', 
            version='0.1.0', 
            py_modules=['kandilli'], 
            platforms='any',
            name='kandilli',)

setup(**config)
