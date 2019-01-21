
# Total number of particles:

F = 'IamAtestFileName'

if F.startswith(('A_', 'B_', 'E_')):
    N = 10 ** 6
elif F.startswith(('CS4_', 'CS5_', 'CS6_', 'DS1_', 'D2_', 'Soft_D2_')):
    N = 10 ** 5
elif F.startswith(('CS1_', 'CS2_', 'CS3_')):
    N = 10 ** 4

if F.startswith(('A_', 'B_', 'CS1_', 'CS4_', 'CS5_', 'CS6_', 'E_')):
    M = 1.  # Total mass equals unity
elif F.startswith(('DS1_', 'D2_', 'Soft_D2_')):
    M = 1. / 6.

m = M / N  # Mass of each particle

if __name__ == '__main__':
    print('N = ', N)
    print('m = ', m)
