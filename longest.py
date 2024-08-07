def longest(s1, s2):
    bitmask_s1 = 0
    bitmask_s2 = 0
    
    for char in s1:
        bitmask_s1 |= 1 << (ord(char) - ord('a'))
    
    for char in s2:
        bitmask_s2 |= 1 << (ord(char) - ord('a'))
    
    combined_bitmask = bitmask_s1 | bitmask_s2
    
    result = []
    for i in range(26):  
        if combined_bitmask & (1 << i):
            result.append(chr(i + ord('a')))
    
    result.sort()

    return ''.join(result)
