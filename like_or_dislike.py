from preloaded import Like, Dislike, Nothing

def like_or_dislike(lst):
    
    current_status = 'Nothing'
    for i in range(0, len(lst)):
        if current_status != lst[i]:
            current_status = lst[i]
        else:
            current_status = 'Nothing'
    return current_status
   
