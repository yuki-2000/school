# -*- coding: utf-8 -*-
"""
Created on Sun Dec  5 13:30:36 2021

@author: yuki
"""

import glob
import os
import re
import shutil

dirs = glob.glob("IMG_8058/*")
for file in dirs:
    name = os.path.basename(file)
    num = int(re.sub(r"\D", "", name))
    if num%100 == 1:
        shutil.copy2(file, "IMG_8058_101/")
        
        
    