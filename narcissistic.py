def narcissistic(number):
    
    digits = [int(d) for d in str(number)]
    num_digits = len(digits)
    return number == sum(d ** num_digits for d in digits)
