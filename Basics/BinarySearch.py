def binary_search(data,target):
    low = 0
    high = len(data) - 1

    while low <= high:
        mid = (low + high) // 2
        if data[mid] == target:
            return True
        elif (target < data[mid]):
            high = mid - 1
        else:
            low = mid + 1
    return False


def recursive_binary_search(data,target):
    if len(data) == 0: return False
    mid = (0 + len(data)-1) // 2 
    if data[mid] == target:
        return True
    elif data[mid] > target:
        return recursive_binary_search(data[0:mid],target)
    else:
        return recursive_binary_search(data[mid+1:],target)


print(recursive_binary_search([1,2,3,4],3))