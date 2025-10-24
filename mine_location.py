def mine_location(field):
    row = len(field)
    column = len(field[0])
    location = []
    for i in range(row):
        for j in range(column):
            if field[i][j] == 1:
                location.append(i)
                location.append(j)
    return location
