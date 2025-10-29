def get_the_vowels(word):
    vowels = ['a', 'e', 'i', 'o', 'u']
    target_idx = 0   # start looking for 'a'
    count = 0

    for ch in word:
        if ch == vowels[target_idx]:
            print(vowels[target_idx])
            count += 1
            target_idx = (target_idx + 1) % len(vowels)

    return count
