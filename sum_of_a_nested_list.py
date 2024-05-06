
#Implement a function to calculate the sum of the numerical values in a nested list. For example :

#sum_nested([1, [2, [3, [4]]]]) -> 10


def sum_nested(lst):
    total_sum = 0
    for element in lst:
        if isinstance(element, list):
            total_sum += sum_nested(element) 
        else:
            total_sum += element
    return total_sum
