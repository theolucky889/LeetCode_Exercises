class Solution(object):
    def heightChecker(self, heights):
        """
        :type heights: List[int]
        :rtype: int
        """
        # create the sorted heights to later be compared
        expected = sorted(heights)
        # returns the total of number of position where heights(h1) is not equal to expected(h2)
        return sum(h1 != h2 for h1, h2 in zip(heights, expected))   # zip() = create pairs of heights and expected heights to compare

solution = Solution()
print(solution.heightChecker([1,1,4,2,1,3]))
print(solution.heightChecker([5,1,2,3,4]))
print(solution.heightChecker([1,2,3,4,5]))