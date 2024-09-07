def get_min_max(seq): 
    for i in range(len(seq)):
        for j in range(i+1, len(seq)):
            if seq[i] > seq[j]:
                temp = seq[i]
                seq[i] = seq[j]
                seq[j] = temp
    return (seq[0], seq[-1]) if len(seq) > 1 else (seq[0], seq[0])
