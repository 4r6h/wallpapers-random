#!/usr/bin/env python3

import os
import urllib.request

from random import *

directory = os.getcwd()

num = int(input("Number of images : "))
res = str(input("Resolution of images : "))
for i in range(num):
    url = "https://random.imagecdn.app/"+res
    filename = directory+"/images/image-{}.png".format(i)
    urllib.request.urlretrieve(url, filename)
