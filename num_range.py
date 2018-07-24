class Solution:
    # @param A : list of integers
    # @param B : integer
    # @param C : integer
    # @return an integer
    def numRange(self, A, B, C):
        n = len(A)
        sets = []
    
        for i in range(n):
            sum = 0
            j = i
    
            while sum < B and j < n:
                sum += A[j]
                j += 1
    
            while sum >= B and sum <= C and j <= n:
                if sum <= C:
                    if A[i:j]:
                        sets.append(A[i:j])
                if j < n:
                    sum += A[j]
                j += 1
    
        return len(sets)