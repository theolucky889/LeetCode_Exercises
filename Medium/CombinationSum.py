class CombSum(object):
    def combinationSum(self, candidates, target):
        """
        :type candidates: List[int]
        :type target: int
        :rtype: List[List[int]]
        """
        # this backtrack function will explore all the possible combinations
        def backtrack(start, target, path):  # current index = start, current target = target, current path = path
            if target == 0: # If target becomes zero, it means the combination has been found
                result.append(path) # add the combination to the result
                return
            if target < 0:  # if the target is less than zero, means the current combination is invalid
                return
            for i in range(start, len(candidates)):
                backtrack(i, target - candidates[i], path + [candidates[i]])

        result = []
        candidates.sort()
        backtrack(0, target, [])
        return result