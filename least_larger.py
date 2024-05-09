# Description is not great, but let me try
# you will get an array of numbers and an index,
# you have to return the index of least larger number than the number at given index, for example:
# ( [4, 1, 3, 5, 6], 0 )
# 4 is the number at given index which is 0
# so what numbers are greater than 4 (5 and 6)
# but the least largest is 5 (so return the index of 5 which is 3)
# if you don't have any numbers greater than the number at the given index return -1

def least_larger(array, i):
    try:
        return array.index(array[i] + 1)
    except:
        return -1
