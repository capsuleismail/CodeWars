def check(string):
    if len(string)>=5:
        return string[::-1]
    return string

def spin_words(sentence):
    return ' '.join([check(word) for word in sentence.split()])
