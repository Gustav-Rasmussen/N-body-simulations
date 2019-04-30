
import re
# import matplotlib.pyplot as plt


def regex_underscore(s):
    p = '(\w*)'
    for i in range(s.count('_')):
        p += '(_[-\w\.]*)'
    return p


def repl_upper(m):
    groupLst = []
    for i in range(1, len(m.groups())):
        if re.match(r'^_[a-zA-Z]', m.groups()[i]):
            groupLst += m.groups()[i].title()[1:]
        else:
            groupLst += m.groups()[i]
    return m.groups()[0] + ''.join(groupLst)


def regex_sub_upper(s):
    return re.sub(regex_underscore(s), repl_upper, s)

# ----------------------------------------------------------------


'''
def regex_letter_underscore(s):
    p = '(\w*)'
    for i in range(s.count('_')):
        p += '([a-zA-Z]+_)'
    return p


def repl_remove_trailing_underscore(m):
    groupLst = []
    for i in range(1, len(m.groups())):
        if re.match(r'^_[a-zA-Z]', m.groups()[i]):
            groupLst += m.groups()[i].title()[1:]
        else:
            groupLst += m.groups()[i]
    return m.groups()[0] + ''.join(groupLst)


def regex_sub_underscore(s):
    return re.sub(regex_letter_underscore(s), repl_remove_trailing_underscore, s)
'''


# test strings ---------------------------------------------------

test_upper = 0
test_cls = 0

S1 = 'AHQ10000_G1.0_5_005NewRmiddleVThetaSigmathetaGamma_-3.00'
S2 = 'AHQ10000_G0.8_47_005LargeRmiddleVPhiSigmaphi_R_middle_19.95'


s1 = "ax1.plot(data[:, 0], data[:, 1],color = 'r',ls = '--',lw=2,ms=7)"
s2 = "ax2.plot(data[:, 0], data[:, 1], color = 'g',ls = '--',lw=2,ms=7)"
s3 = "ax3.plot(data[:, 0], data[:, 1], color= 'k',ls = '--',lw=2,ms=7)"

s4 = "ax4.plot(data[:, 0], data[:, 1], color ='b', ls =  ':',lw=2,ms=7)"
s5 = "ax5.plot(data[:, 0], data[:, 1], color = 'g', ls =  ':',lw=2,ms=7)"
s6 = "ax6.plot(data[:, 0], data[:, 1], color = 'k', ls =  ':',lw=2,ms=7)"

s7 = "ax7.plot(data[:, 0], data[:, 1], color = 'Brown',ls = '--',lw=2,ms=7)"
s8 = "ax8.plot(data[:, 0], data[:, 1], color = 'Orange',ls = '--',lw=2,ms=7)"

s9 = "ax9.plot(data[:, 0], data[:, 1], color = 'Brown', ls =  ':',lw=2,ms=7)"
s10 = "ax10.plot(data[:, 0], data[:, 1], color = 'Orange',ls = '--',lw=2,ms=7)"

pattern_1 = re.compile(r"'\w'\s*,\s*ls\s*=\s*'")
sub_pattern = re.compile(r"'\s*,\s*ls\s*=\s*'")

# res = pattern.findall()

'''
x = [2, 4, 6, 8, 10]
y = [4, 16, 36, 64, 100]
# plt.plot(x, y, color="Brown", ls=':')
plt.plot(x, y, "Brown", ls=":")
plt.show()
'''


def main():
    if test_upper:
        print(S1,
              regex_sub_upper(S1),
              S2,
              regex_sub_upper(S2))
        # return regex_sub_upper(s1), regex_sub_upper(s2)
    if test_cls:
        '''
        for i in range(1, 11):
            exec(f'print(s{i})')
        '''
        if re.findall(pattern_1, s1):
            print(s1)
            # print(s1.replace("',ls = '", ''))
            print(re.sub(sub_pattern, '', s1))
        '''
        if re.findall(pattern_1, s4):
            print(s4)
            print(s4.replace("',ls = '", ''))
        if re.findall(pattern_1, s7):
            print(s7)
            print(s7.replace("',ls = '", ''))
        '''
        return


if __name__ == '__main__':
    main()
