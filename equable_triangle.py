import math
def equable_triangle(a,b,c):
    if a + b <= c or a + c <= b or b + c <= a:
        return False
    
    perimeter = a + b + c
    
    s = perimeter / 2
    
    area = math.sqrt(s * (s - a) * (s - b) * (s - c))
    
    return area == perimeter
