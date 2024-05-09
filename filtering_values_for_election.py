# A specialist of statistics was hired to do an investigation about the people's voting intention for a certain candidate for the next elections.

# Unfortunately, some of the interviewers, hired for the researches, are not honest and they want to modify the results because, some of them like the candidate too much, or others hate him.

# The specialist suspects about the situation and will apply his own method named: Recursive 2.5 Standard Deviation Filter.

# He does not know who of them are cheating and obviously, he doesn´t know the minimum or maximum possible votes for this candidate.
# Rules:
# 1.The method works with the following steps explained below:
# 2.The method calculates the mean,  μ, and the standard deviation, σ for the received data that has n elements.
# 3.A new data is obtained discarding all the values that are not in the range [μ - 2.5σ, μ + 2.5σ] (strictly lower or higher than these extremes)
# 4.The values of  μ and σ are recalculated and an all the values will be filtered by the new range with the updated values of  μ and σ and so on.
# 5.He receives the data from the interviewers. The data is the number of votes of samples less than 500 people per neighbourhood of a county.



def average(lst):

    return sum(lst) / len(lst)


def standard_devation(lst):
    a = average(lst)
    st_dv = (sum([(value - a)**2 for value in lst]) / len(lst))
    return st_dv**0.5


def filter_val(lst):
    len_a = len(lst)
    while True:
        avg = average(lst)
        st_d = standard_devation(lst)
        filtered = [data for data in lst if avg -
                    2.5 * st_d <= data <= avg + 2.5 * st_d]
        if filtered == lst:
            break
        else:
            lst = filtered
    len_b = len(lst)
    mean = average(lst)
    st_d = standard_devation(lst)
    return [[len_a, len_b], mean, st_d]


lists = [35, 34, 37, 32, 33, 36, 38, 32, 35, 35, 36, 34, 35, 100, 85, 70]
print(filter_val(lists))
