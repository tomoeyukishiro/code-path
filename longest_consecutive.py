class Solution:
    # @param A : tuple of integers
    # @return an integer
    def longestConsecutive(self, A):
        A = sorted(A)
        max_cnt = 0
        cnt = 1
        for i in range(len(A)-1):
            if A[i+1] - A[i] == 1:
                cnt += 1
            if max_cnt < cnt:
                max_cnt = cnt
                cnt = 0
        return max_cnt