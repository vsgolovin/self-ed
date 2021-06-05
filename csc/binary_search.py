def main():
    # read array to search elements in
    array = list(map(int, input().split()[1:]))

    # read elements to search for
    nums = list(map(int, input().split()[1:]))

    # find and display elements' indices
    indices = [index(num, array) for num in nums]
    output = [str(ind + 1) if ind >= 0 else '-1' for ind in indices]
    print(' '.join(output))


def index(k, lst):
    """
    Return index of element `k` in a sorted list of integers `lst`
    or `-1` if `k` is not in `lst`.
    """
    a = 0
    b = len(lst) - 1
    while b >= a:
        ind = a + (b - a) // 2
        if lst[ind] > k:
            b = ind - 1
        elif lst[ind] < k:
            a = ind + 1
        else:  # found k
            return ind
    return -1  # did not find k


if __name__ == '__main__':
    main()

