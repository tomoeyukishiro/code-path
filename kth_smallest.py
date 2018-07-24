class Solution:
    # @param A : tuple of integers
    # @param B : integer
    # @return an integer
    def findSmallest(self, A, skip):
        smallest_i = -1
        for i in range(len(A)):
            if i not in skip:
                if smallest_i == -1 or A[i] < A[smallest_i]:
                    smallest_i = i
        return smallest_i
    
    def kthsmallest(self, A, k):
        skip = []
        for j in range(k):
            smallest_i = self.findSmallest(A, skip)
            skip.append(smallest_i)
        return A[smallest_i]