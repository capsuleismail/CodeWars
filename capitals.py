def capitals(word):
    result = []
    for i in range(len(word)):
        if word[i].isupper():
            result += [i]  

    return result
