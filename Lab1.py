def print_array_elements(arr):
    for element in arr:
        print(element)

def print_length(arr):
    return len(arr)

def get_value_at_index(arr, index):
    if 0 <= index < len(arr):
        return arr[index]
    else:
        return None

def replace_index_value(arr, index, value):
    if 0 <= index < len(arr):
        arr[index] = value
        return arr
    else:
        return -1

my_array = [1,2,3,4,5,6,7]
print('The index')
idx = int(input())

print('The value for replacement')
replacement = int(input())



array_at_index = get_value_at_index(my_array,idx)

print_array_elements(my_array)
result = print_length(my_array)
print(result)
print(array_at_index)
result1 = replace_index_value(my_array,idx,replacement)
print(result1)
