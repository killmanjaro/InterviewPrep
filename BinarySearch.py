
# uses divide and conquer approach
# O(logn)

def binary_search(arr, low, high, x):
    # check base case
    if high >= low:
        mid = (high + low) // 2

        # check middle
        if arr[mid] == x:
            print(x,"is at the middle")
            return mid
        # if element is smaller than middle, then check lower half

        if arr[mid] > x:
            print(x,"is less than the middle,",arr[mid],"searching for",x,"between:",arr[low],arr[mid-1])
            return binary_search(arr, low, mid-1, x)
        # else check upper half
        else:
            print(x,"is more than the middle,",arr[mid],"searching for",x,"between:",arr[mid+1],arr[high])
            return binary_search(arr, mid+1, high, x)
    else:
        return -1


arr = [1, 2, 3, 5, 7, 10, 12]
x = 2

result = binary_search(arr, 0, len(arr)-1, x )
if result != -1:
    print("element is present at endex", result)
else:
    print("not present")