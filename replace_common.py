def replace_common(st, letter):
    freq = {}
    for ch in st:
        if ch.isalpha():
            ch = ch.lower()  # optional, for case-insensitivity
            if ch in freq:
                freq[ch] += 1
            else:
                freq[ch] = 1

    to_replace = max(freq, key=freq.get)

    return st.replace(to_replace, letter)
