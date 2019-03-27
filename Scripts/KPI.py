#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Mar 27 16:43:38 2019

@author: gustavcollinrasmussen
"""

import os
import subprocess
import datetime

line_count = "cat {} | wc -l"
PEP8_count = "pep8 {} | wc -l"


def byte_to_str(byte_str):
    string = byte_str.decode('utf-8').lstrip().rstrip()
    return string


with open('KPI.txt', 'a') as wf:
    wf.write(str(datetime.datetime.now())+"\n\n")
    wf.write("Module name, number of lines, PEP-8 violations:\n")
    file_count = 0
    for root, dirs, files in os.walk("."):
        # files = files.sort()
        # print(type(files))
        # print(files[0])
        for filename in files:
            if ((filename in (".DS_Store", "KPI.log"))
                | any(x in filename for x in [".pyc", ".txt"])):
                continue
            lines = subprocess.check_output(line_count.format(filename), shell=True)
            PEP8 = subprocess.check_output(PEP8_count.format(filename), shell=True)
            # res_str = f"{filename}, {lines.decode('utf-8').lstrip().rstrip()}, {}"
            res_str = f"{filename}, {byte_to_str(lines)}, {byte_to_str(PEP8)}\n"
            wf.write(res_str)
            file_count += 1
    
    wf.write(f"\nNumber of Python scripts: {file_count}\n\n")
