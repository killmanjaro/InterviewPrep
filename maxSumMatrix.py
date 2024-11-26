

# Python3 program to find the maximum value 
# of top N/2 x N/2 matrix using row and 
# column reverse operations 
  
  
def maxSum(matrix): 
    n = len(matrix) // 2
    #print(n)
  
    sum = 0
    indices = []
    for i in range(n): 
        for j in range(n): # for all values in the matrix
        

            top_left = (matrix[i][j], (i,j))
            top_right = (matrix[i][2*n-j-1], (i, 2*n-j-1))
            bottom_left = (matrix[2*n-i-1][j], (2*n-i-1, j))
            bottom_right = (matrix[2*n-i-1][2*n-j-1], (2*n-i-1, 2*n-j-1 ))
            #print("my vals are:",top_left, top_right, bottom_left, bottom_right )
  
            # We can replace current cell [i, j] 
            # with 4 cells without changing/affecting 
            # other elements. 
            max_sum, max_ind = max(top_left, top_right, bottom_left, bottom_right, key=lambda x: x[0])

            sum += max_sum
            indices.append(max_ind)



  
    return sum, indices
  
  
# Driver Code 
if __name__ == "__main__": 
  
    mat = [[112, 42, 83, 119], 
           [56, 125, 56, 49], 
           [15, 78, 101, 43], 
           [62, 98, 114, 108]] 
  
    print(maxSum(mat)) 