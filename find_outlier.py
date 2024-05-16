def find_outlier(integers):
    if len(list(filter(lambda x: not x%2==0, integers)))==1:
        return list(filter(lambda x: not x%2==0, integers))[0]
    return list(filter(lambda x: x%2==0, integers))[0]

# quite ugly, I'll refactor this one, promise.
