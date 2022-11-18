# Write a program that returns the sum of an array [1, 2, 3, 4, 5].

def _sum(arr):
    if len(arr) == 1:
        return arr[0]
    else:
        return arr[0] + _sum(arr[1:])

arr_elements = [1, 21, 25, 39, 25, 78, 35]
print('The sum of an array is: {}'.format(_sum(arr_elements)))