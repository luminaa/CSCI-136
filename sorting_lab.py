'''
Question:
List_1 = [2, 5, 6, 8, 9, 10, 7, 3]
A) Given the list, List_1 above, write a quick sort function that partitions the list in such a way that:

All even numbers come before all odd numbers.
Even numbers are sorted in ascending order and odd numbers are sorted in descending order. 

B) Given the list above i.e. List_1, implement a quick sort function using Python and select the first element as the pivot
C) Given the list above i.e. List_1, implement a quick sort function using Python and select the last element as the pivot
'''

def split_even_odd(lst):
    even = []
    odd = []
    for i in lst:
        if i % 2 == 0:
            even.append(i)
        else:
            odd.append(i)
    return even, odd

def quick_sort_first(lst, order):
    if len(lst) <= 1:
        return lst
    pivot = lst[0]
    left = []
    right = []
    for i in range(1, len(lst)):
        if order == "asc":
            if lst[i] < pivot:
                left.append(lst[i])
            else:
                right.append(lst[i])
        elif order == "desc":
            if lst[i] > pivot:
                left.append(lst[i])
            else:
                right.append(lst[i])
    return quick_sort_first(left, order) + [pivot] + quick_sort_first(right, order)

def quick_sort_last(lst, order):
    if len(lst) <= 1:
        return lst
    pivot = lst[-1]
    left = []
    right = []
    for i in range(0, len(lst) - 1):
        if order == "asc":
            if lst[i] < pivot:
                left.append(lst[i])
            else:
                right.append(lst[i])
        elif order == "desc":
            if lst[i] > pivot:
                left.append(lst[i])
            else:
                right.append(lst[i])
    return quick_sort_last(left, order) + [pivot] + quick_sort_last(right, order)




list_1 = [2, 5, 6, 8, 9, 10, 7, 3]
even, odd = split_even_odd(list_1)
print(even)
print(odd)
sorted_even = quick_sort_first(even, "asc")
sorted_odd = quick_sort_first(odd, "desc")
print(sorted_even + sorted_odd)

print()
print(quick_sort_first(list_1, "asc"))
print(quick_sort_last(list_1, "asc"))