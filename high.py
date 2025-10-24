def high(x):
    
    convert = dict((chr(i), i - 96) for i in range(97, 123))


    text_split = x.split()
    storage = []
    for word in text_split:
        storage.append(sum(list(map(lambda x: convert[x], word))))
#     
    return text_split[storage.index(max(storage))]
