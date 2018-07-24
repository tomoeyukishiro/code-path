class Solution:
    # @param A : integer
    # @return a list of list of integers
    def prettyPrint(self, num):
    
        m = n = 2*num -1
        k = 0
        l = 0
        i = 0
    
        matrix = [[0 for _ in range(n)] for _ in range(m)]
    
        while k < m and l < n :  
            for i in range(l, n) :      
                if matrix[k][i] == 0:
                    matrix[k][i] = num
    
            k += 1
    
            for i in range(k, m) :         
                if matrix[i][n-1]==0:
                    matrix[i][n-1] = num
            n -= 1
    
            if (k<m):
                for i in range(n-1, l-1, -1):
                    if matrix[m-1][i] == 0:
                        matrix[m-1][i] = num
            m -= 1
    
            if (l<n):
                for i in range(m-1, k-1, -1):
                    if matrix[i][l] == 0:
                        matrix[i][l] = num
            l += 1
    
            num -= 1

        return matrix
