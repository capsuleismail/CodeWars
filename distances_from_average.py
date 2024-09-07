def distances_from_average(test_list):
    mean = sum(test_list) /len(test_list)
    return list(map(lambda x: round(mean-x, 2), test_list))
