#!/usr/bin/env python
"""osx_audio.py

Functions to simplify gathering and setting OS X audio settings

Author: Michael J. Smalley <michaeljsmalley@gmail.com>

"""

from Foundation import *
import re
from time import sleep
import osx_version

version = osx_version.get_version_name()
angle_brackets = "<>"

def get_audio_state():
    """Returns a dictionary containing audio state"""
    return { 'level': get_volume_level() ,
             'mute': get_mute_state()
           }

def get_volume_level():
    if version == 'Mountain Lion':
        script = NSAppleScript.alloc().initWithSource_("output volume of (get volume settings)")
        state, _ = script.executeAndReturnError_(None)
        _, volume = str(state).strip(angle_brackets).split() 
        return volume

def get_mute_state():
    if version == 'Mountain Lion':
        script = NSAppleScript.alloc().initWithSource_("output muted of (get volume settings)")
        state, _ = script.executeAndReturnError_(None)
        _, mute_state = str(state).strip(angle_brackets).split() 
        mute_state = re.search(r"\"([A-Za-z0-9_]+)\"", mute_state)
        if mute_state.group(1) == "true":
            mute_state = True
        elif mute_state.group(1) == "false":
            mute_state = False
        return mute_state

def set_mute_state( bool ):
    if version == 'Mountain Lion':
        script = NSAppleScript.alloc().initWithSource_("set volume output muted " + str(bool))
        script.executeAndReturnError_(None)
        return get_mute_state()

def set_volume_level( int ):
    if version == 'Mountain Lion':
        script = NSAppleScript.alloc().initWithSource_("set volume output volume " + str(int))
        script.executeAndReturnError_(None)
        return get_volume_level()

if __name__ == "__main__":
    print get_audio_state()
