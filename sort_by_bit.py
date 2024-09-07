def sort_by_bit(arr):
    return arr.sort(key=lambda x: (bin(x).count('1'), x))

## 6, Algorithms
