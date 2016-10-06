#!/usr/bin/env python
""" Downloades images from URLs in a text file.

the text file is given as the first argument and must contain 
an URL in each line. The images are either saved in the 
current directory or in a given local path.
"""

import sys
import urllib

__author___ = "Souheil Dehmani"
__version__ = "1.0.0"
__maintainer__ = "Souheil Dehmani"
__email__ = "souheil.dehmani@gmail.com"
__status__ = "Prototype"

# set to the desired path to save the downloaded images. Leave empty to save in current directory
local_path = ""

def download_images():
    with open(sys.argv[1], 'r') as url_file:
        success = 0    # counter for successful donwloads 
        fail = 0       # counter for failed downloads
        for line in url_file:
            image_url = line
            try:
                urllib.urlretrieve(image_url, local_path + "image_" + str(success) + ".jpg")
                success += 1

            except IOError as err:
                print(err)   # something wrong with the given local path or URL
                fail += 1
			
        print str(success) + " images saved with success"
        print str(fail) + " failures" 
		
if __name__ == "__main__":
    download_images()