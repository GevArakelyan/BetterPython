

# %%

class UnionFind:
    def __init__(self, n) -> None:
        self.up_bound = list(range(n))
        self.rank = [0]*n

    def find(self, x_index):
        if self.up_bound[x_index] == x_index:
            return x_index
        self.up_bound[x_index] = self.find(self.up_bound[x_index])
        return self.up_bound[x_index]

    def union(self, xindex, yindex):
        rx = self.find(xindex)
        ry = self.find(yindex)
        if (rx == ry):
            return False
        if self.rank[rx] == self.rank[ry]:
            self.rank[rx] += 1
            self.up_bound[ry] = rx
        elif self.rank[rx] > self.rank[ry]:
            self.up_bound[ry] = rx
        else:
            self.up_bound[rx] = ry
        return True




#%%
# finding max element and it's index
# tuple comparison is in lexicographical order.
A = [2, 1, 3, 4]
print(max((tab_i, i) for i, tab_i in enumerate(A)))
# most common element of an array
# n is the number of words k is the max length of a word. O(nk) on average,
# but O(n*n*k) in the worst case.



def majority(L):
    count = {}
    for word in L:
        if word in count:
            count[word] += 1
        else:
            count[word] = 1

    val_1st_max, arg_1st_max = min((-count[word], word) for word in count)
    return arg_1st_max


def closest_values(L):
    assert len(L) >= 2
    L.sort()
    valmin, index = min((L[i] - L[i-1], i) for i in range(1, len(L)))
    return L[index-1], L[index]

# sometimes sorting in O(n) | counting sort | pigeonhole sort.
