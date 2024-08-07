def solution(s):
    store = 0
    roman = {'I': 1, 'V': 5, 'X': 10, 'L': 50, 'C': 100, 'D': 500,
             'M': 1000, 'IV': 4, 'IX': 9, 'XL': 40, 'XC': 90, 'CD': 400, 'CM': 900}
    index = 0
    limit = len(s)
    for i in range(limit):
        if (i + 1) < limit and roman[s[i]] < roman[s[i + 1]]:
            store -= roman[s[i]]
        else:
            store += roman[s[i]]

    return store
