import array as arr
# 1) Create a function to calculate the mean of a list:
#    a) Add all elements using a loop.
#    b) Mean = total sum / number of elements.
#    c) Return the mean as a float.

def mean(lst):
    total = 0
    for num in lst:
        total += num
    return total / len(lst)

# 2) Create a function to calculate the median of a list:
#    a) Sort the list first.
#    b) If the size is odd, return the middle element.
#    c) If the size is even, return the average of the two middle elements.

def median(lst):
    sorted_lst = sorted(lst)
    n = len(sorted_lst)
    if n % 2 == 1:
        return sorted_lst[n // 2]
    else:
        mid1 = sorted_lst[n // 2 - 1]
        mid2 = sorted_lst[n // 2]
        return (mid1 + mid2) / 2

# 3) Create a sample list and find its size using `len()`.

sample_list = [1, 2, 3, 4, 5]
size = len(sample_list)

# 4) Call both functions and print the mean and median.
print("Mean:", mean(sample_list))
print("Median:", median(sample_list))


