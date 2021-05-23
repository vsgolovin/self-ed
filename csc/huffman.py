def main():
    # read input
    s = input()
    freq = dict()  # character frequencies
    for ch in s:   # count characters
        if ch not in freq:
            freq[ch] = 1
        else:
            freq[ch] += 1

    # dictionary of binary codes
    codes = dict()
    for ch in freq:
        codes[ch] = ''

    # generate Huffman code for every letter
    while (len(freq) > 2):
        # extract 2 smallest frequencies and corresponding letters
        key1 = key_min(freq)
        val1 = freq.pop(key1)
        key2 = key_min(freq)
        val2 = freq.pop(key2)

        # modify codes for these letters
        for ch in key1:
            codes[ch] = '0' + codes[ch]
        for ch in key2:
            codes[ch] = '1' + codes[ch]

        # add entry with all extracted letters
        # and a sum of their frequencies
        freq[key1 + key2] = val1 + val2

    # one or two last entries
    i = 0
    for letters in freq:
        for ch in letters:
            codes[ch] = str(i) + codes[ch]
        i += 1

    # encode input string
    es = ''.join([codes[ch] for ch in s])

    # display number of characters in input string
    # and encoded string length
    print(len(codes), len(es))

    # display Huffman codes
    for letter, code in codes.items():
        print(f'{letter}: {code}')

    # print encoded input string
    print(es)


def key_min(d):
    "Get dictionary key corresponding to the smallest value."
    val_min = None
    key_min = None
    for key, val in d.items():
        if val_min is None or val < val_min:
            val_min = val
            key_min = key
    return key_min


main()
