# -*- coding: utf-8 -*-
"""
Created on Thu Nov 25 13:32:02 2021

@author: meric
"""


import pathlib



data_dir = pathlib.Path("./flowers/flowers")
image_count = len(list(data_dir.glob('*/*.jpg')))
print(image_count)








