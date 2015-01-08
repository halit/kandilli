try:
    from setuptools import setup
except ImportError:
    from distutils.core import setup

REQUIREMENTS = [i.strip() for i in open("requirements.txt").readlines()]

config = dict(description='Kandilli last earthquakes api',
            long_description=open('README.md').read(),
            author='Halit Alptekin',
            url='https://github.com/halitalptekin/kandilli', 
            author_email='info@halitalptekin.com', 
            license='MIT',
            keywords='api, earthqueke, earthquakes', 
            version='0.1.1', 
            py_modules=['kandilli'], 
            platforms='any',
            name='kandilli',
            install_requires=REQUIREMENTS)

setup(**config)
