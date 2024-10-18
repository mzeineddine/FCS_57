def bst_search (arr, x, start, end):
    if end >= start:
        mid = (end+start)//2
        if arr[mid] == x:
            return True
        elif arr[mid] < x:
            return bst_search(arr, x,mid+1, end)
        else:
            return bst_search(arr, x,start, mid-1)
    else:
        return False

arr = [1,2,3,4,5,6,7,8,9]

print(bst_search(arr, 6, 0, len(arr)-1))