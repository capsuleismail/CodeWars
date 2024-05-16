def find_missing_letter(chars):
    expected_sum = sum(range(ord(chars[0]), ord(chars[-1]) + 1))
    
    
    actual_sum = sum(ord(char) for char in chars)
    
    missing_letter_ascii = expected_sum - actual_sum
    
    return chr(missing_letter_ascii)
