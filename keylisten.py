#!/usr/bin/env python

from getkey import getkey, keys

while True:
    try:
        key = getkey()
        print(keys.name(key))
    except KeyboardInterrupt:
        print("Quitting...")
        break