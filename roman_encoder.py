def solution(n):
    n = n+1
    res = []
    while n > 1000:
        n = n - 1000
        res.append('M')
    while n > 900:
        n = n - 900
        res.append('CM')
    while n > 500:
        n = n - 500
        res.append('D')
    while n > 400:
        n = n - 400
        res.append('CD')
    while n > 100:
        n = n - 100
        res.append('C')
    while n > 90:
        n = n - 90
        res.append('XC')
    while n > 50:
        n = n - 50
        res.append('L')
    while n > 40:
        n = n - 40
        res.append('XL')
    while n > 10:
        n = n - 10
        res.append('X')
    while n > 9:
        n = n - 9
        res.append('IX')
    while n > 5:
        n = n - 5
        res.append('V')
    while n > 4:
        n = n - 4
        res.append('IV')
    while n > 1:
        n = n - 1
        res.append('I')
    return ''.join(r for r in res)
