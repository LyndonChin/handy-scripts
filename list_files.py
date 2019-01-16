#!/usr/bin/python
# -*- coding: UTF-8 -*-

import os
import shutil

for root, dirs, files in os.walk("/Volumes/ryou/books", topdown=False):
    for name in files:
        print('* [  ] ' + name)
