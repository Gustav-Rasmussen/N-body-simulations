F = 'IamAtestFileName'

# Total number of particles:
if F.startswith(('A_', 'B_', 'E_', 'Soft_B_')):
    N = 10 ** 6
elif F.startswith(('CS4_', 'CS5_', 'CS6_', 'DS1_', 'D2_', 'Soft_D2_',
                   'IIc', 'IId', 'IId', 'Test_')):
    N = 10 ** 5
elif F.startswith(('CS1_', 'CS2_', 'CS3_')):
    N = 10 ** 4

# Declare total mass
if F.startswith(('A_', 'B_', 'CS1_', 'CS4_', 'CS5_', 'CS6_', 'E_',
                 'Soft_B_', 'Test_', 'IIc_CS4_', 'IIc_CS5_', 'IIc_CS6_',
                 'IIc_Test_CS4', 'IId_CS4')):
    M = 1.  # Total mass equals unity
elif F.startswith(('DS1_', 'D2_', 'Soft_D2_', 'IIc_Soft_D2_', 'IIc_DS1_',
                   'IId_Soft_D2_')):
    M = 1. / 6.

# Define particle mass
m = M / N

if __name__ == '__main__':
    print(f'{N= } \n',
          f'{m= }')
