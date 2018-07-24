class Solution:
    # @param A : integer
    # @return a list of list of integers
    def prettyPrint(self, num):
    
        m = n = 2*num -1 ##    m x n matrix , length of each row and column
        k = 0 # row start counter
        l = 0 # column start counter
        i = 0 # iterator
    
        matrix = [[0 for _ in range(n)] for _ in range(m)]
    
        while k < m and l < n :  
            #insert the first row
            for i in range(l, n) :      
                if matrix[k][i] == 0:
                    matrix[k][i] = num   # row index constt, change values in columns
    
            k += 1   # first row printed, so increment row start index
    
            #insert the last column
            for i in range(k, m) :         
                if matrix[i][n-1]==0:
                    matrix[i][n-1] = num   # column index constt, change values in rows
            n -= 1   # last column printed, so decrement num of columns
    
            #insert the last row
            if (k<m):   #  if row index less than number of rows remaining
                for i in range(n-1, l-1, -1):
                    if matrix[m-1][i] == 0:
                        matrix[m-1][i] = num   # row index constt, insert in columns
            m -= 1   # last row printed, so decrement num of rows
    
            #insert the first column
            if (l<n):    #  if column index less than number of columns remaining
                for i in range(m-1, k-1, -1):
                    if matrix[i][l] == 0:
                        matrix[i][l] = num # column index constt, insert in rows
            l += 1      # first column printed, so increment column start index
    
            num -= 1    # all elements of value A inserted , so decrement
    
        return matrix
