def change(st):
    result = []
    st = st.lower()
    for letter in [chr(i) for i in range(97, 123)]:
        if letter in st:
            result.append('1')
        else:
            result.append('0')
    return ''.join(result)
