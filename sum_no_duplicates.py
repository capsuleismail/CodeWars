def sum_no_duplicates(l):
    seen = set()
    duplicates = set()
    for i in l:
        if i in seen:
            duplicates.add(i)
        seen.add(i)
            
            
    return sum([item for item in l if item not in duplicates])
