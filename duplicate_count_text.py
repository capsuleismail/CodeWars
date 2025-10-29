def duplicate_count_text(text):
    text = text.lower()
    result = []
    #return len([x for x in set(text.lower()) if text.lower().count(x)>1]) 
    for i in range(len(text)):
        if text.count(text[i]) > 1 and text[i] not in result:
            print(text[i])
            result.append(text[i])
    return len(result)
