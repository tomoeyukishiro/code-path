class Solution:
    # @param A : list of integers
    # @return a list of integers
    def nextGreater(self, A):
        result = []
        if len(A) == 1:
            result.append(-1)
            return result
        for i in range(len(A)):
            cnt = 0
            for j in range(i+1, len(A)):
                if A[j] > A[i] and cnt < 1:
                    cnt += 1
                    result.append(A[j])
            if cnt < 1:
                result.append(-1)
        return result
