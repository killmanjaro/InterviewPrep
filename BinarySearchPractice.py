
#11/24/2024
'''
def BinarySearch(arr, low, high, x):

    if high >= low:
        # base case, create middle
        middle = (high + low)// 2

        # check middle
        if arr[middle] == x:
            return middle

        # check right side, call BS
        elif x > arr[middle]:
            return BinarySearch(arr, middle+1, high, x)


        # check left side, call BS
        else:
            return BinarySearch(arr, low, middle-1, x)

    else:
        return -1
    

arr = [1, 2, 5, 7, 8, 10, 12]
x = 8
return_val = BinarySearch(arr, 0, len(arr)-1, x)
print(return_val)
'''

# 11/25/2024

def BS(arr, low, high, x):
    # base case
    if high >= low:

        # initialize middle
        mid = (high + low) //2

        if x == arr[mid]:
            return mid

        # check left
        elif x < arr[mid]:
            return BS(arr, low, mid-1, x)

        # check right
        else:
            return BS(arr, mid+1, high, x)

    else:
        return -1
    

arr = [1, 2, 3, 4, 5]
x = -2
result = BS(arr, 0, len(arr)-1, x)
print(result)