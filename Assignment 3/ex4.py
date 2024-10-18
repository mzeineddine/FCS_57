def insert_inSorted(list, val, start, end):
    if val > list[end]:
        list.insert(end+1, val)
    elif val < list[start]:
        list.insert(start, val)
    else:
        mid = (start+end)//2
        if val > list[mid]:
            #insert_right
            insert_inSorted(list, val, mid+1, end)
        else:
            #insert_left
            insert_inSorted(list, val, start, mid-1)

list1=[ 1,3,56,234,789]
val = 789

insert_inSorted(list1, val, 0, len(list1)-1)
print(list1)