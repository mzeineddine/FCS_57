def gen(arr,n, str = ""):
    if n == 0:
        print(str)
    else:
        for i in arr:
            str1 = str+i
            gen(arr, n-1, str1)

arr = ['a', 'b', 'c']

gen(arr, 3)