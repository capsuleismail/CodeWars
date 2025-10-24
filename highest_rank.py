def highest_rank(arr):
#     if not arr:
#         return None  # NOEMPTYAEEAY WILL BE GIVEN

    arr.sort()  # sorting groups duplicates together
    length = len(arr)
    
    max_freq = 1 # MINIMUM FREQUENT ELEMENT 
    most_freq = arr[0] #ASSUMING THAT THE MOST FREQUENT ELEMENT IS THE FIRST ONE
    index = 0
    
    
    while index < length:
        count = 1
        
        # Count occurrences of the current number
        while (index + 1 < length) and (arr[index] == arr[index + 1]):
            count += 1
            index += 1
        
        # Update the most frequent number
        if count > max_freq:
            max_freq = count
            most_freq = arr[index]
        elif count == max_freq:
            # If same frequency, pick the larger number
            most_freq = max(most_freq, arr[index])
        
        index += 1  # move to the next distinct number
    
    return most_freq
        
