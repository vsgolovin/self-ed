def main():
    n = int(input())  # number of commands
    h = BinaryHeap()
    for _ in range(n):
        inp = input()
        if inp == 'ExtractMax':
            print(h.extract_max())
        else:
            cmd, num = inp.split()
            assert cmd == 'Insert'
            h.insert(int(num))

class BinaryHeap(object):
    "Binary max heap with items stored inside a `list`."
    def __init__(self):  # should have used list as a base class
        self.items = []
        self.length = 0
        return None

    def __len__(self):
        return self.length

    def insert(self, a):
        """
        Insert element `a` into heap.
        Returns index of inserted element.
        """
        self.items.append(a)
        self.length += 1
        ind = self._sift_up(self.length - 1)
        return ind

    def extract_max(self):
        "Extract the largest element from heap."
        if self.length == 0:
            return None

        # swap root (max) element with last
        indlast = self.length - 1
        self._swap(0, indlast)

        # remove last element
        amax = self.items.pop()
        self.length -= 1

        # sift down element that was moved to the root
        self._sift_down(0)
        return amax

    def _sift_up(self, ind):
        while ind > 0:
            pind = self._parent_ind(ind)
            if self.items[pind] < self.items[ind]:
                self._swap(pind, ind)
                ind = pind
            else:
                break
        return ind

    def _sift_down(self, ind):
        while True:
            # get indices of child nodes
            cind1, cind2 = self._child_inds(ind)

            # compare values of child nodes
            # or detect end of heap
            if cind1 is None:
                return ind
            elif (cind2 is None
                  or self.items[cind1] > self.items[cind2]):
                cind = cind1
            else:
                cind = cind2

            # compare node to largest of its children
            if self.items[ind] < self.items[cind]:
                self._swap(ind, cind)
                ind = cind
            else:
                return ind

    def _swap(self, i1, i2):
        "Swap heap elements with indices `i1` and `i2`."
        self.items[i1], self.items[i2] = self.items[i2], self.items[i1]
        return None

    def _parent_ind(self, ind):
        if ind == 0:
            return None
        return (ind + 1) // 2 - 1

    def _child_inds(self, ind):
        ind += 1
        ind1, ind2 = 2 * ind - 1, 2 * ind
        if ind1 > self.length - 1:
            return None, None
        elif ind2 > self.length - 1:
            return ind1, None
        return ind1, ind2
 
if __name__ == '__main__':
    main()
