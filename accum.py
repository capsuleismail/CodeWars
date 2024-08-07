def accum(st):
    
    result = []
    for i in range(len(st)):
        result += [f'{st[i]*(i+1)}'.capitalize()]
    return '-'.join(result)
