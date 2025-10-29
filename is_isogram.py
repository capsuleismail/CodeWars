def is_isogram(string):
    
    string = string.lower()
    result = []
    for i in range(len(string)):
        if string[i] not in result:
            result.append(string[i])
        
    return ''.join(result) == string
