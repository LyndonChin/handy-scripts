#!/usr/bin/python
# -*- coding: UTF-8 -*-

import os
import shutil

for root, dirs, files in os.walk("/Volumes/ryou/pdfs/", topdown=False):
    for name in files:
        if (name.endswith('.jpg')):
            file_path = os.path.join(root, name)
            print("moving " + file_path)
            shutil.move(file_path, os.path.join('/Volumes/ryou/pdfs', name))
    for name in dirs:
        shutil.rmdir(os.path.join(root, name))
