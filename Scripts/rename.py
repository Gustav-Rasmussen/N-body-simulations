import os
from pathlib import Path
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
txtFilePath = Path.cwd().parent / 'textFiles'

sims = ['A', 'B', 'CS1', 'CS2', 'CS3', 'CS4', 'CS5', 'CS6', 'D2', 'DS1', 'E',
        'MartinICandFinalEddandOM', 'softD2']

folders = [f'{txtFilePath}/{i}' for i in sims]

for i in sims:
    vars()[i] = f'{txtFilePath}/{i}'


def rename_files(files):
    for f in files:
        if f == '.DS_Store':
            continue
        file_name, file_ext = os.path.splitext(f)
        # print(file_name)
        if 'Hernquist' in file_name:
            file_name = file_name.replace('Hernquist', 'HQ')
        if 'Hq' in file_name:
            file_name = file_name.replace('Hq', 'HQ')
        if 'Osipkov' in file_name:
            file_name = file_name.replace('Osipkov', 'O')
        if 'Merritt' in file_name:
            file_name = file_name.replace('Merritt', 'M')
        if ('LargeRMiddle' in file_name) and ('RMiddle' in file_name):
            file_name = file_name.replace('LargeRMiddle', '')
            file_name = file_name.replace('RMiddle', 'LargeRMiddle')
        if ('Sigmarad' in file_name):
            file_name = file_name.replace('rad', 'R')
        if ('Sigmatan' in file_name):
            file_name = file_name.replace('tan', 'T')
        if ('phi' in file_name):
            file_name = file_name.replace('phi', 'Phi')
        if ('theta' in file_name):
            file_name = file_name.replace('theta', 'Theta')
        if ('Gamma_-1.50' in file_name):
            file_name = file_name.replace('Gamma_-1.50', 'Gamma_-1.5')
        if ('Gamma_-2.00' in file_name):
            file_name = file_name.replace('Gamma_-2.00', 'Gamma_-2.0')
        if ('Gamma_-2.50' in file_name):
            file_name = file_name.replace('Gamma_-2.50', 'Gamma_-2.5')
        if ('Gamma_-3.00' in file_name):
            file_name = file_name.replace('Gamma_-3.00', 'Gamma_-3.0')
        new_name = regexUpper.regex_sub_upper(file_name)
        new_file = f'{new_name}{file_ext}'
        # print(f'{new_file}')
        os.rename(f, new_file)


'''
modules = ["readVDF_2_new", "fileLsts", "readVDF2", "VDFnetwork", "readVDF",
           "TimeEvolutionGammaKappaBeta", "Sigma", "readVDF_2_new"
           ]

readfile = f'{modules[0]}.txt'
writefile = f'{modules[0]}_copy.txt'

# print(readfile, writefile)

with open(readfile, "r") as rf:
    with open(writefile, "w") as wf:
        for line in rf:
            if 'Eddington' in line:
                line = line.replace('Eddington', 'Edd')
            if 'perturbation' in line:
                line = line.replace('perturbation', 'Pert')
            if 'Hernquist' in line:
                line = line.replace('Hernquist', 'HQ')
            if 'Hq' in line:
                line = line.replace('Hq', 'HQ')
            if 'Osipkov_Merritt' in line:
                line = line.replace('Osipkov_Merritt', 'OM')
            if 'Osipkov' in line:
                line = line.replace('Osipkov', 'O')
            if 'Merritt' in line:
                line = line.replace('Merritt', 'M')
            if 'figure_path' in line:
                line = line.replace('figure_path', 'figurePath')
            if 'datalist_innerbin' in line:
                line = line.replace('datalist_innerbin', 'bin1')
            if 'datalist_first_middlebin' in line:
                line = line.replace('datalist_first_middlebin', 'bin2')
            if 'datalist_second_middlebin' in line:
                line = line.replace('datalist_second_middlebin', 'bin3')
            if 'datalist_outerbin' in line:
                line = line.replace('datalist_outerbin', 'bin4')
            if 'list_of_files_' in line:
                line = line.replace('list_of_files_', 'FileLst')
            if 'innerbin_' in line:
                line = line.replace('innerbin_', 'bin1')
            if 'first_middlebin_' in line:
                line = line.replace('first_middlebin_', 'bin2')
            if 'second_middlebin_' in line:
                line = line.replace('second_middlebin_', 'bin3')
            if 'outerbin_' in line:
                line = line.replace('outerbin_', 'bin4')
            if 'radial_bins' in line:
                line = line.replace('radial_bins', 'RBins')
            if 'R_limit' in line:
                line = line.replace('R_limit', 'Rlim')
            if 'Almost_Final' in line:
                line = line.replace('Almost_Final', 'SecondLast')
            if any(x in line for x in ['Sigmarad', 'sigmarad']):
                line = line.replace('rad', 'R')
            if any(x in line for x in ['Sigmatan', 'sigmatan']):
                line = line.replace('tan', 'T')
            if ('phi' in line):
                line = line.replace('phi', 'Phi')
            if ('theta' in line):
                line = line.replace('theta', 'Theta')
            if ('_new_R_middle_' in line):
                line = line.replace('_new_R_middle_', '')
            if ('large_R_middle_19_95_' in line):
                line = line.replace('large_R_middle_19_95_', 'bin5')
            if ('large_R_middle_31_62_' in line):
                line = line.replace('large_R_middle_31_62_', 'bin6')
            if ('_large_R_middle_' in line):
                line = line.replace('_large_R_middle_', '')
            if '\'/Users/gustav.c.rasmussen' in line:
                line = line.replace('\'/Users/gustav.c.rasmussen',
                                    'os.getcwd() + \'')
            wf.write(line)
'''

with change_dir(A):
    # print(os.listdir())
    rename_files(os.listdir())

'''
with change_dir(B):
    rename_files(os.listdir())

with change_dir(CS1):
    rename_files(os.listdir())

with change_dir(CS2):
    rename_files(os.listdir())

with change_dir(CS3):
    rename_files(os.listdir())

with change_dir(CS4):
    rename_files(os.listdir())

with change_dir(CS5):
    rename_files(os.listdir())

with change_dir(CS6):
    rename_files(os.listdir())

with change_dir(DS1):
    rename_files(os.listdir())

with change_dir(D2):
    rename_files(os.listdir())

with change_dir(E):
    rename_files(os.listdir())

with change_dir(softD2):
    rename_files(os.listdir())

print(len(os.listdir()))
'''