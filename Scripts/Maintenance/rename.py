import os
# from pathlib import Path
import re
import regexUpper
from contextlib import contextmanager

# regexUpper.main()  # check module is working


@contextmanager
def change_dir(destination):
    try:
        cwd = os.getcwd()
        os.chdir(destination)
        yield
    finally:
        os.chdir(cwd)


# txtFilePath = Path.cwd() / 'Desktop/GperturbNew/StableStructures/textFiles'
# txtFilePath = Path.cwd().parent / 'textFiles'

sims = ['A', 'B', 'CS1', 'CS2', 'CS3', 'CS4',
        'CS5', 'CS6', 'D2', 'DS1', 'E', 'MartinICandFinalEddandOM', 'softD2']

modules = ["readVDF_2_new", "fileLsts", "readVDF2", "VDFnetwork", "readVDF",
           "TimeEvolutionGammaKappaBeta", "Sigma", "readVDF_2_new"]

# folders = [f'{txtFilePath}/{i}' for i in sims]

'''
for i in sims:
    vars()[i] = f'{txtFilePath}/{i}'
'''

file_name = ''
line = ''
# readfile = f'{modules[2]}.txt'
# writefile = f'{modules[2]}_copy.txt'
readfile = 'testfile.txt'
writefile = 'testfile_copy.txt'

filename_dict = {'Hernquist': 'HQ',
                 'Hq': 'HQ',
                 'Osipkov': 'O',
                 'Merritt': 'M',
                 'phi': 'Phi',
                 'theta': 'Theta',
                 'Gamma_-1.50': 'Gamma_-1.5',
                 'Gamma_-2.00': 'Gamma_-2.0',
                 'Gamma_-2.50': 'Gamma_-2.5',
                 'Gamma_-3.00': 'Gamma_-3.0'
                 }

line_dict = {'Eddington': 'Edd',
             'perturbation': 'Pert',
             'Hernquist': 'HQ',
             'Hq': 'HQ',
             'Osipkov_Merritt': 'OM',
             'Osipkov': 'O',
             'Merritt': 'M',
             'figure_path': 'figurePath',
             'datalist_innerbin': 'bin1',
             'datalist_first_middlebin': 'bin2',
             'datalist_second_middlebin': 'bin3',
             'datalist_outerbin': 'bin4',
             'list_of_files_': 'FileLst',
             'innerbin_': 'bin1',
             'first_middlebin_': 'bin2',
             'second_middlebin_': 'bin3',
             'outerbin_': 'bin4',
             'radial_bins': 'RBins',
             'R_limit': 'Rlim',
             'Almost_Final': 'SecondLast',
             'phi': 'Phi',
             'theta': 'Theta',
             '_new_R_middle_': '',
             'large_R_middle_19_95_': 'bin5',
             'large_R_middle_31_62_': 'bin6',
             '_large_R_middle_': '',
             '\'/Users/gustav.c.rasmussen': 'os.getcwd() + \'',
             'Red': 'r',
             'Green': 'g',
             'Black': 'k',
             'Blue': 'b',
             '_average_inside_bin_': '_BinAvg_',
             '_avg_in_bin_': '_BinAvg_',
             'average_': 'avg_',
             'color=': '',
             'color =': '',
             ' )': ')',
             'data, label': 'data, _'
             }


def find_replace_multi_ordered(string, dictionary):
    # sort keys by length, in reverse order
    for item in sorted(dictionary.keys(), key=len, reverse=True):
        string = re.sub(item, dictionary[item], string)
    return string


s = "HEREABCISABCACSAMPLEABCSTRING"
d = {"C": "-", "ABC": "-", "CSAMPLEABC": "-:)-"}
# find_replace_multi_ordered(s, d)


def file_replace(From: str, to: str, in_str: str = ''):
    """."""
    if in_str in file_name:
        return file_name.replace(From, to)
    return file_name


def rename_files(files):
    for f in files:
        if f == '.DS_Store':
            continue
        file_name, file_ext = os.path.splitext(f)
        # print(file_name)
        # for k, v in filename_dict.items():
        #     file_name = file_replace(k, v)
        file_name = find_replace_multi_ordered(file_name, filename_dict)
        file_name = file_replace('rad', 'R', 'Sigmarad')
        file_name = file_replace('tan', 'T', 'Sigmatan')
        if ('LargeRMiddle' in file_name) and ('RMiddle' in file_name):
            file_name = file_name.replace('LargeRMiddle', '')
            file_name = file_name.replace('RMiddle', 'LargeRMiddle')
        new_name = regexUpper.regex_sub_upper(file_name)
        new_file = f'{new_name}{file_ext}'
        # print(f'{new_file}')
        os.rename(f, new_file)


def line_replace(From: str, to: str, in_str: str = ''):
    """."""
    if in_str in line:
        return line.replace(From, to)
    return line


def replace_lines():
    with open(readfile, "r") as rf:
        with open(writefile, "w") as wf:
            for line in rf:
                # for k, v in line_dict.items():
                #     line = line_replace(k, v)
                line = find_replace_multi_ordered(line, line_dict)
                # line = line_replace('yan', '', 'cyan')
                # line = line_replace('agenta', '', 'magenta')
                # line = line_replace('hite', '', 'white')
                if any(x in line for x in ['Sigmarad', 'sigmarad']):
                    line = line.replace('rad', 'R')
                if any(x in line for x in ['Sigmatan', 'sigmatan']):
                    line = line.replace('tan', 'T')
                # if label, ls: swap to ls, label.
                # Put ls and color together.
                if re.findall(regexUpper.pattern_1, line):
                    print(line)
                    # print(re.sub(regexUpper.sub_pattern, '', line))
                    line = re.sub(regexUpper.sub_pattern, '', line)
                    print(line)
                wf.write(line)


def main():
    # print(readfile, writefile)
    replace_lines()
    '''
    print(len(os.listdir()))
    with change_dir(sims[0]):
        # print(os.listdir())
        rename_files(os.listdir())
    '''


if __name__ == '__main__':
    main()
