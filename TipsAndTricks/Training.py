# string
from numpy import append


str = "hello Gevorg"
strlist = list(str)
print(str)
print(strlist)

strlist.extend(" jan")
print(strlist)

strfromlist = ''.join(strlist)
print(strfromlist)


# Lists

#%%%
def append_number(num, numbers=[]):
    numbers.append(num)
    print(num) 
    print(numbers)
    return numbers

x = append_number(1)
y = append_number(2)

#%%
x = [1, 2, 3]
x[0] = 3
# we can do this also x.extend([3, True, 'Hi'])
# x.append("Hello")
x.pop()

elem = 3
# functions
len(x)
sorted(x)
x.sort()
x.count(elem)
if (elem in x):
    print(elem)
x.append(elem)
x.pop() #extracts and returns last elem. 

# copy operation
y = x    
z = x[:]

x[0] = "Changed x"

print(x)
print(y)
print(z)

# Dictionary | behind it thre is a hash table ==> complexity
# of the x in d, d[x], d[x]=2 is in practice constant time, even 
# if the worst case is linear
d = {} # empty dictionary
d = {'the': 3, 'is': 4}



# Tuples are immutable
x = (1,2,3)
x = (2,) # tuple of one elem
x = () # tuple of 0 elem or x = tuple()
# tuple can serve as a key in dictionary







# Iteration over collections
for i in range(3):
    print(i)
x = [1,2,3,5,3]

for index, value in enumerate(x):
    print(index, value)

# range interface [ stop ]  [ start , stop] [ start, stop, step]
for index in range(len(x)):
    value = x[index]
    print(index, value)

d = {'the': 3, 'is': 4}
for key, val in d.items():
    print(key, val)




# list and dictionary comprehensions, Iterators

n = 3
squire_numbers = [ x **2 for x in range(n+1)]
print(squire_numbers)

t = [0 for _ in range(n)]
print(t)

# ..
str = "cowboy bebop"
nb_occurrences = { letter: 0 for letter in str}
print(nb_occurrences)

# Ranges and Other Iterators
# range(k,n) from k to n-1
# range(k, n , 2) from k to n-1 two by two
# range(n-1, -1, -1) from n-1 to 0 in decreasing order


# Any function can serve as an iterator, as long
# as it can produce elements at different moments of its execution using the keyword
# yield.
# def all_pairs(L):
# n = len(L)
# for i in range(n):
#   for j in range(i + 1, n):
#       yield (L[i], L[j])
#---------------------------------------------------------------------------------------------------------------


# %%
