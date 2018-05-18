


def binary_search_iter(arr, item):
    low, high = 0, len(arr) -1

    while low <= high:
        mid = (low + high) // 2
        guess = arr[mid]
        if guess == item:
            return mid
        if guess > item:
            high = mid - 1
        else:
            low = mid + 1
    return None




def binary_search(arr, item):
    '''
    working on a recursive definition
    currently returns the wrong index (index of item in sub-array)
    '''
    low = 0 
    high = len(arr)
    #import pdb; pdb.set_trace()
    middle = (low + high) // 2

    guess = arr[middle]
    #import pdb; pdb.set_trace()
    if guess == item:
        return middle
    if guess > item:
        return binary_search(arr[low : middle], item)
    else:
        return binary_search(arr[middle : high], item)

if __name__ == '__main__':
    print(binary_search([1,2,3,4,5,6], 5))
