def duplicate_encode(word):
    word = word.lower()
    result = ''
    count = {}
    for i in range(len(word)):
        if word[i] in count:
            count[word[i]] += 1
        else:
            count[word[i]] = 1
            
    for element in word:
        if count[element] > 1:
            result += ")"
        else:
            result += "("
    return result
