def find_it(seq):
    
    for number in seq:
        value = seq.count(number)
        if value % 2 == 0:
            continue
        return number
