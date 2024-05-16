def solution(s):
    s = s + '_'
    return list(map(''.join, zip(*[iter(s)]*2)))
