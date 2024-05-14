def fiver(number):
    result = []
    while number > 0:
        digit = number % 10  
        
        result.append(digit)  
        number //= 10 
    return True if 5 in result else False
    


def dont_give_me_five(start,end):
    excepted = 0
    for i in range(start, end+1):
        #make sure to catch negative numbers with abs()
        if fiver(abs(i)) == False:
            print(i)
            excepted += 1
        else:
            excepted += 0
    return excepted
