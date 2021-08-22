# Sweep line technique
# Example -- Intersection of Intervals

# Given n intervals [i,ri) for i = 0, . . . ,n − 1, we wish to find a value x included
# in a maximum number of intervals. Here is a solution in time O(n log n).
# %%
import os
def max_interval_insersect(S):
    B = ([(left, +1) for left, right in S] +
         [(right, -1) for left, right in S])
    B.sort()
    c = 0
    best = (c, None)
    for x, d in B:
        c += d
        if best[0] < c:
            best = (c, x)
        return best

# Note that the order of processing of the elements of B
# gaurantees that the right endpoints of the intervals are handled before the left endpoints of the intervals,
# which is necessary when dealing with intervals that are 
# half-open to the right.

# %%
dirs = os.listdir()
dirs.sort(reverse=True)
dirs
# %%
