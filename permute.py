class Solution:
    # @param A : list of integers
    # @return a list of list of integers
    def permute(self, A):
        solutions = [[]]

        for num in A:
            next = []
            for solution in solutions:
                for i in range(len(solution) + 1):
                    candidate = solution[:i] + [num] + solution[i:]
                    if candidate not in next:
                        next.append(candidate)

            solutions = next

        return solutions