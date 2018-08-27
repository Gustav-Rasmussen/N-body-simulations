
import re


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

s1 = 'AHQ10000_G1.0_5_005NewRmiddleVThetaSigmathetaGamma_-3.00'
s2 = 'AHQ10000_G0.8_47_005LargeRmiddleVPhiSigmaphi_R_middle_19.95'


def main():
    print(s1,
          regex_sub_upper(s1),
          s2,
          regex_sub_upper(s2))

    # return regex_sub_upper(s1), regex_sub_upper(s2)


if __name__ == '__main__':
    main()
