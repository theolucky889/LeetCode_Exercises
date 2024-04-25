'''
46. Permutations
Medium
Topics
Companies
Given an array nums of distinct integers, return all the possible permutations. You can return the answer in any order.

 

Example 1:

Input: nums = [1,2,3]
Output: [[1,2,3],[1,3,2],[2,1,3],[2,3,1],[3,1,2],[3,2,1]]
Example 2:

Input: nums = [0,1]
Output: [[0,1],[1,0]]
Example 3:

Input: nums = [1]
Output: [[1]]
 

Constraints:

1 <= nums.length <= 6
-10 <= nums[i] <= 10
All the integers of nums are unique.
'''
# define a class named 'Solution' that will contain our method
class Solution(object):
    # define a method named 'permit' that takes a list of integers 'nums'
    def permute(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        results = []    # will store all the permutation
        
        # helper function for backtracking
        def backtrack(start=0): # nested function inside 'permute' 
            # if at the last element, append the permutation copy
            if start == len(nums):  # to check if the start index has reached the length of nums, if true, complete the permutation
                results.append(nums[:]) # append the permutation into the result list
                return
            # loop through the arrays to swap each element to the next
            for i in range(start, len(nums)):
                # swap the current number with the start
                nums[start], nums[i] = nums[i], nums[start]
                # recurse on the next part of the array 
                backtrack(start + 1)
                # swap to original position for backtrack (ensure no duplicates)
                nums[start], nums[i] = nums[i], nums[start]
        
        backtrack()     # call to the backtrack function
        return results
    
# call out class Solution for output
solution = Solution()
print(solution.permute([1,2,3]))
print(solution.permute([0,1]))
print(solution.permute([1]))

