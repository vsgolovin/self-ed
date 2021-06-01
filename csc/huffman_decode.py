def main():
    # first line: [number of letters] [encoded string length]
    k, _ = map(int, input().split())

    # read letters and their Huffman codes
    # and store them in a tree accordingly
    tree = [None, None]
    for _ in range(k):
        letter, code = input().split(': ')
        tree = add_leaf(letter, code, tree)

    # decode input string
    encoded = input()
    decoded = decode(encoded, tree)
    print(decoded)


def add_leaf(letter, code, tree):
    if len(code) > 1:
        index = int(code[0])
        if tree[index] is None:
            tree[index] = [None, None]
        tree[index] = add_leaf(letter, code[1:], tree[index])
    else:
        tree[int(code)] = letter
    return tree


def decode(encoded, tree):
    branch = tree
    decoded = []
    for ch in encoded:  # ch is either '0' or '1'
        branch = branch[int(ch)]
        if isinstance(branch, str):
            decoded.append(branch)
            branch = tree  # reset tree traversal
    return ''.join(decoded)
 

main()

