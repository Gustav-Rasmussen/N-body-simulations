#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Oct 13 11:59:26 2018

@author: gustavcollinrasmussen
"""

from pathlib import Path
import os


def exec_terminal_cmd(path):
    os.system("cd " + str(Path.cwd()) + "\"" + path + "\"")


if __name__ == '__main__':
     print(os.getcwd())
     print(Path.cwd())
     path = '/Desktop/GperturbNew/StableStructures/pythonScripts'
     exec_terminal_cmd(path)
