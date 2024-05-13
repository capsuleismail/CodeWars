# Odd bits are getting ready for Bits Battles.
# Therefore the n bits march from right to left along an 8 bits path. 
# Once the most-significant bit reaches the left their march is done. Each step will be saved as an array of 8 integers.
# Return an array of all the steps.




def bit_march (num):
    base = [0] * (8-num) + [1] * num 
    result = []
    while base[0] != 1:
        result.append(base[:])
        base = base[1:]+[base[0]]
        print(base)
    result.append(base)
        
    return result
