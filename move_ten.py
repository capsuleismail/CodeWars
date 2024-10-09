def move_ten(st):
    result = ''
    for char in st:
        if 'a' <= char <= 'z':
            char_index = ord(char) - ord('a')
            
            new_index = (char_index + 10) % 26
            new_char = chr(new_index + ord('a'))
            result += new_char
        else:
            result += char

    return result
