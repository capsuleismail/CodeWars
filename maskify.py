# return masked string
def maskify(cc):

    length = len(cc)
    return '#'*(length - 4) + cc[-4:]
