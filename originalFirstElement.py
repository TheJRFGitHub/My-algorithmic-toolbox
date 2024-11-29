
first = 0
array = [8,10,15,3,6]
left = 0
right = len(array) - 1

while left + 1 < right:

    '''
    print(f"left: {left}")
    print(f"right: {right}")
    
    '''
    mid = (left + right) // 2

    if array[left] < array[mid] and array[mid] < array[right]:
        first = array[0]
        break
    if array[left] > array[mid] and array[mid] < array[right]:
        right = mid
    else:
        left = mid


if first == 0:
    if array[left] < array[right]:
        first = array[left]
    else:
        first = array[right]

print(f"Original first element: {first}")
