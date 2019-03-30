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
    string = byte_str.decode("utf-8").lstrip().rstrip()
    return string


with open("KPI.txt", "a") as wf:
    wf.write(
        "------------------------------------------------------------\n\n"
    )
    wf.write(str(datetime.datetime.now()) + "\n\n")
    KPI_list = []
    wf.write(
        "Module name,\t number of lines,\t PEP-8 violations:".rjust(50)
        + "\n\n"
    )
    file_count = 0
    for root, dirs, files in os.walk("."):
        for filename in files:
            if (filename in (".DS_Store", "KPI.log")) | any(
                x in filename for x in [".pyc", ".txt"]
            ):
                continue
            lines = subprocess.check_output(
                line_count.format(filename), shell=True
            )
            PEP8 = subprocess.check_output(
                PEP8_count.format(filename), shell=True
            )
            # res_str = f"{filename}, {lines.decode('utf-8').lstrip().rstrip()}, {}"
            # res_str = f"{filename}, {byte_to_str(lines)}, {byte_to_str(PEP8)}\n"
            KPI_list.append(
                {
                    "module": f"{filename}",
                    "lines": int(byte_to_str(lines)),
                    "PEP8_violations": int(byte_to_str(PEP8)),
                }
            )
            file_count += 1
        KPI_list_sorted = sorted(
            KPI_list, key=lambda KPI: KPI["lines"], reverse=True
        )
    for element in KPI_list_sorted:
        res_str = f"{element['module']}\t{element['lines']}\t{element['PEP8_violations']}"
        wf.write(res_str.rjust(50) + "\n")
        # print(f"{element['module']}{element['lines']:^40}{element['PEP8_violations']:>10}")
        # f"{left_aligned:<15}{center:^10}{right_aligned:>15}"
        # wf.write(f"{element['module']}, {element['lines']}, {element['PEP8_violations']}\n")

    wf.write(f"\nNumber of Python scripts: {file_count} \n\n")
