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

sims = ['A',
        'B',
        'CS1',
        'CS2',
        'CS3',
        'CS4',
        'CS5',
        'CS6',
        'D2',
        'DS1',
        'E',
        'MartinICandFinalEddandOM',
        'softD2'
        ]

modules = ["readVDF_2_new",
           "fileLsts",
           "readVDF2",
           "VDFnetwork",
           "readVDF",
           "TimeEvolutionGammaKappaBeta",
           "Sigma",
           "readVDF_2_new"
           ]

# folders = [f'{txtFilePath}/{i}' for i in sims]

'''
for i in sims:
    vars()[i] = f'{txtFilePath}/{i}'
'''


def file_replace(from: str, to: str, in_str=from: str):
    """."""
    if in_str in file_name:
        return file_name.replace(from, to)
    return file_name


def rename_files(files):
    for f in files:
        if f == '.DS_Store':
            continue
        file_name, file_ext = os.path.splitext(f)
        # print(file_name)

        file_name = file_replace('Hernquist', 'HQ')
        file_name = file_replace('Hq', 'HQ')
        file_name = file_replace('Osipkov', 'O')
        file_name = file_replace('Merritt', 'M')
        file_name = file_replace('rad', 'R', 'Sigmarad')
        file_name = file_replace('tan', 'T', 'Sigmatan')
        file_name = file_replace('phi', 'Phi')
        file_name = file_replace('theta', 'Theta')
        file_name = file_replace('Gamma_-1.50', 'Gamma_-1.5')
        file_name = file_replace('Gamma_-2.00', 'Gamma_-2.0')
        file_name = file_replace('Gamma_-2.50', 'Gamma_-2.5')
        file_name = file_replace('Gamma_-3.00', 'Gamma_-3.0')

        if ('LargeRMiddle' in file_name) and ('RMiddle' in file_name):
            file_name = file_name.replace('LargeRMiddle', '')
            file_name = file_name.replace('RMiddle', 'LargeRMiddle')

        new_name = regexUpper.regex_sub_upper(file_name)
        new_file = f'{new_name}{file_ext}'
        # print(f'{new_file}')
        os.rename(f, new_file)


def line_replace(from: str, to: str, in_str=from: str):
    """."""
    if in_str in line:
        return line.replace(from, to)
    return line


def replace_lines():
    with open(readfile, "r") as rf:
        with open(writefile, "w") as wf:
            for line in rf:
                line = line_replace('Eddington', 'Edd')
                line = line_replace('perturbation', 'Pert')
                line = line_replace('Hernquist', 'HQ')
                line = line_replace('Hq', 'HQ')
                line = line_replace('Osipkov_Merritt', 'OM')
                line = line_replace('Osipkov', 'O')
                line = line_replace('Merritt', 'M')
                line = line_replace('figure_path', 'figurePath')
                line = line_replace('datalist_innerbin', 'bin1')
                line = line_replace('datalist_first_middlebin', 'bin2')
                line = line_replace('datalist_second_middlebin', 'bin3')
                line = line_replace('datalist_outerbin', 'bin4')
                line = line_replace('list_of_files_', 'FileLst')
                line = line_replace('innerbin_', 'bin1')
                line = line_replace('first_middlebin_', 'bin2')
                line = line_replace('second_middlebin_', 'bin3')
                line = line_replace('outerbin_', 'bin4')
                line = line_replace('radial_bins', 'RBins')
                line = line_replace('R_limit', 'Rlim')
                line = line_replace('Almost_Final', 'SecondLast')
                line = line_replace('phi', 'Phi')
                line = line_replace('theta', 'Theta')
                line = line_replace('_new_R_middle_', '')
                line = line_replace('large_R_middle_19_95_', 'bin5')
                line = line_replace('large_R_middle_31_62_', 'bin6')
                line = line_replace('_large_R_middle_', '')
                line = line_replace('\'/Users/gustav.c.rasmussen',
                                    'os.getcwd() + \'')
                # Use plt color codes.
                line = line_replace('Red', 'r')
                line = line_replace('Green', 'g')
                line = line_replace('Black', 'k')
                line = line_replace('Blue', 'b')
                line = line_replace('yan', '', 'cyan')
                line = line_replace('agenta', '', 'magenta')
                line = line_replace('hite', '', 'white')
                line = line_replace('_average_inside_bin_', '_BinAvg_')
                line = line_replace('_avg_in_bin_', '_BinAvg_')
                line = line_replace('average_', 'avg_')
                line = line_replace('color=', '')
                line = line_replace('color =', '')
                line = line_replace(' )', ')')
                line = line_replace('data, label', 'data, _')
                line = line_replace('', '')
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
    readfile = f'{modules[2]}.txt'
    writefile = f'{modules[2]}_copy.txt'
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
