#!/usr/bin/env python

import sys
import urllib

local_adress = "~/blue/"


with open(sys.argv[1], 'r') as urls_file:
    i = 1
    for line in urls_file:
        image_url = line
        try:
            urllib.urlretrieve(image_url, "image_" + str(i) + ".jpg")
        except IOError as err:
            print(err)   # something wrong with local path
        i += 1

