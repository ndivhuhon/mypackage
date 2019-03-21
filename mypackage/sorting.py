def bubble_sort(items):
    count = 0
    
    for idx in range(len(items)-1):
        if items[idx] > items[idx + 1]:
            items[idx],items[idx + 1] = items[idx + 1],items[idx]
            count += 1
            
    if count == 0:
        
        return items
    else:
        
        return bubbleSort(items)

def merge(left, right):
  
    left_index, right_index = 0, 0
    result = []
    while left_index < len(left) and right_index < len(right):
        if left[left_index] < right[right_index]:
            result.append(left[left_index])
            left_index += 1
        else:
            result.append(right[right_index])
            right_index += 1

    result += left[left_index:]
    result += right[right_index:]
    return result


def merge_sort(items):
    
    if len(items) <= 1:  # base case
        return items

    # divide array in half and merge sort recursively
    half = len(items) // 2
    left = merge_sort(items[:half])
    right = merge_sort(items[half:])

    return merge(left, right)

def quick_sort(items):
    if (len(items) < 2):
        return items
    else:
        pivot = items[0]
        rest = items[1:]
        low = [each for each in rest if each < pivot]
        high = [each for each in rest if each >= pivot]
        return quick_sort(low) + [pivot] + quick_sort(high)
