def dynamic_sliding_window(arr, k):
    # k is the value we are comparing against
    n = len(arr)
    size_of_window = 1
    min_size_window = float('inf')
    ceiling = 1
    floor = 0
    while ceiling != n:
        print(arr[floor:ceiling])
        print(floor, ceiling)
        if sum(arr[floor:ceiling]) >= k:
            if ceiling - floor < min_size_window:
                min_size_window = ceiling - floor
                if min_size_window == 1:
                    return min_size_window
            floor += 1
        else:
            ceiling += 1

    return min_size_window



arr = [4,2,2,7,8,1,2,8,1,0]
k = 8
print(dynamic_sliding_window(arr, k))


            
        
    
