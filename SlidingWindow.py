
def sliding_window(arr, k):
    # k is the size of our fixed k
    n = len(arr)
    cur_sum = 0
    max_sum = float("-inf")
    for i in range(n-k+1):
        cur_sum = sum(arr[i:i+k])
        if cur_sum > max_sum:
            max_sum = cur_sum

    return max_sum


arr = [1, 4, 2, 10, 2, 3, 1, 0, 20]
k = 4

max_sum = sliding_window(arr, k)
print(max_sum)

        
