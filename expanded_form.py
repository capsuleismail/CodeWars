def expanded_form(number):
    return ' + '.join(list(map(str, list(filter(lambda x: x != 0, [(int(s)*10**i) for s, i in zip(str(number), reversed(list(range(len(str(number))))))])))))
