"""
Given the following numbers: 3,5,8,9,5,2,1,4
Write Python code to sort these numbers by implementing merge sort 
"""

def merge_sort(lst):
    if len(lst) <= 1:
        return lst
    else:
        mid = len(lst) // 2
        left = merge_sort(lst[:mid])
        right = merge_sort(lst[mid:])
        return merge(left, right)
    
def merge(left, right):
    result = []
    while len(left) > 0 or len(right) > 0:
        if len(left) > 0 and len(right) > 0:
            if left[0] < right[0]:
                result.append(left.pop(0))
            else:
                result.append(right.pop(0))
        elif len(left) > 0:
            result.append(left.pop(0))
        elif len(right) > 0:
            result.append(right.pop(0))
    return result

print(merge_sort([3,5,8,9,5,2,1,4]))