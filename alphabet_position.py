def alphabet_position(text):
    text = text.lower()
    result = []
    convert = {chr(i).lower():(i-96) for i in range(97, 123)}
    for t in text:
        if t.isalpha():
            result += [str(convert[t])]
    return ' '.join(result)
