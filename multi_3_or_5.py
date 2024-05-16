def solution(number):
    result = 0
    solution = {0:0, 1:0, 2:0, 3:0, 4:3, 5:3, 6:8, 7:14, 8:14, 9:14, 10:23}
    if 0 <= number <= 10: return solution[number]
    if number < 0: return 0
    else:
        for i in range(1, number):
            if i % 3 == 0 or i % 5 == 0:
                result +=  i
    return result
