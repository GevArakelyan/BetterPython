# finding max element and it's index
# tuple comparison is in lexicographical order.
A = [2, 1, 3, 4]
max((tab_i, i) for i, tab_i in enumerate(A))
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
    valmin, index = min((L[i] - L[i-1], i) for i in range(1,len(L)))
    return L[index-1], L[index]

# sometimes sorting in O(n) | counting sort | pigeonhole sort.
