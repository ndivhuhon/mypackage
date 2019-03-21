def bubble_sort(items):
    for i in range(len(items)-1,0,-1):
        for j in range(i):
            if items[j] > items[j+1]:
                temp = items[j]
                items[j] = items[j+1]
                items[j+1] = temp
                return items

def merge_sort(items):
    if len(items) < 2:return items

    result,mid = [],int(len(items)/2)
    y = merge_sort(items[:mid])
    z = merge_sort(items[mid:])

    while (len(y) > 0) and (len(z) > 0):
        if y[0] > z[0]:result.append(z.pop(0))
        else: result.append(y.pop(0))
        result.extend(y+z)
    return result

def quick_sort(items):
    if (len(items) < 2):
        return items
    else:
        pivot = items[0]
        rest = items[1:]
        low = [each for each in rest if each < pivot]
        high = [each for each in rest if each >= pivot]
        return quick_sort(low) + [pivot] + quick_sort(high)
