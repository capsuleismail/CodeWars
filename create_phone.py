def create_phone_number(n):
    res = ''
    total = ''.join(str(d) for d in n)
    a = '(' + ''.join(first for first in total[0:3]) + ')'
    b = ' ' + ''.join(first for first in total[3:6]) + '-'
    c = ''.join(first for first in total[6:11])
    res = a + b + c
    return res
