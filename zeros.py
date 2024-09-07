
def zeros(n: int) -> int:

    if n == 1:
        return 2  
    if n == 2:
        return 2
    if n == 3:
        return 3  
    
    prev2 = 2  
    prev1 = 3  
    
    
    for element in range(3, n):
        current = prev1 + prev2  
        prev2 = prev1   
        prev1 = current  

    return current 
