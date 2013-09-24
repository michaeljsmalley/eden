#!/usr/bin/env python
"""osx_version.py

Functions to simplify gathering OS X version information

Author: Michael J. Smalley <michaeljsmalley@gmail.com>

"""

from platform import mac_ver

version_mappings = {
    '10.9' : 'Mavericks',
    '10.8' : 'Mountain Lion',
    '10.7' : 'Lion',
    '10.6' : 'Snow Leopard',
    '10.5' : 'Leopard',
    '10.4' : 'Tiger',
    '10.3' : 'Panther',
    '10.2' : 'Jaguar',
    '10.1' : 'Puma',
    '10.0' : 'Cheetah'
}

def get_version(): 
    """Returns a dictionary with the name and number of current OS X version"""
    version = '.'.join(mac_ver()[0].split('.')[:2])
    return { 'name': version_mappings[version], 'number': version }

def get_version_name():
    return get_version()['name']

def get_version_number():
    return get_version()['number']

if __name__ == "__main__":
    print get_version()
