"""
Given the following numbers: 3,5,8,9,5,2,1,4
Write Python code to sort these numbers by implementing merge sort 
"""

def merge_sort(lst, order):
    if len(lst) <= 1:
        return lst
    else:
        mid = len(lst) // 2
        left = merge_sort(lst[:mid], order)
        right = merge_sort(lst[mid:], order)
        return merge(left, right, order)
    
def merge(left, right, order):
    result = []
    while len(left) > 0 or len(right) > 0:
        if len(left) > 0 and len(right) > 0:
            if order == 'ascending':
                if left[0] < right[0]:
                    result.append(left.pop(0))
                else:
                    result.append(right.pop(0))
            elif order == 'descending':
                if left[0] > right[0]:
                    result.append(left.pop(0))
                else:
                    result.append(right.pop(0))
        elif len(left) > 0:
            result.append(left.pop(0))
        elif len(right) > 0:
            result.append(right.pop(0))
    return result

print(merge_sort([3,5,8,9,5,2,1,4], 'descending'))

grades = {'Charles': 100, 'Chris': 85, 'Ema': 60, 'Ariel': 65, 'John': 85, 'Patrick': 55, 'Stella': 50, 'Sharon':89, 'Victoria':83, 'Debby':90, 'Suzanne': 78, 'Kevin':76}

student_and_grade_lst = []
for student in grades:
    student_and_grade_lst.append([grades[student], student])

sorted_grades_in_asc = merge_sort(student_and_grade_lst, 'ascending')
print(sorted_grades_in_asc)

sorted_grades_in_desc = merge_sort(student_and_grade_lst, 'descending')
print(sorted_grades_in_desc)