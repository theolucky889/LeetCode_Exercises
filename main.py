from Easy.Height_Checker import Height_Checker  # import module the height checker function from height checker file
from Easy.Two_Sum import TwoSum
from Medium.Permutations import Permutations    # import module permutation function from permutation file
from Medium.CombinationSum import CombSum
from Hard.N_Queen import Queen

def main():

# Height Checker
    # method to callout the function so it will be called later in the loop
    hc = Height_Checker()
    # leetcode question   
    height_list = [     
        [1,1,4,2,1,3], 
        [5,1,2,3,4], 
        [1,2,3,4,5],
    ]
    # loop the lists and print the result
    print('Height Checker Results:')
    for heights in height_list:
       print(hc.heightChecker(heights))

    # method to callout the function so it will be called later in the loop
    perm = Permutations()
    # leetcode question
    nums_list = [
        [1,2,3], 
        [0,1],
        [1]
    ]
    # loop the list and print the result
    print('Permutation Results: ') 
    for nums in nums_list:
        print(perm.permute(nums))

# Combination Sum
    combSum = CombSum()
    candidate_list = [
        [2,3,6,7],
        [2,3,5],
        [2]
    ]
    targets = [7, 8, 1]
    print('Combination Sum: ')
    for candidates, target in zip(candidate_list,targets):
        print(f'For candidates {candidates} with target {target}')
        result = (combSum.combinationSum(candidates, target))
        print(result)
        
# N Queen
    n_Queen = Queen()
    queens = [
        4,
        5
    ]
    print('N-Queens Solution: ')
    for n in queens:
        print(f'\nSolutions for {n} Queens: ')
        solutions = n_Queen.solveNQueens(n)
        for solution in solutions:
            for row in solution:
                print(row)
            print('')

# Two Sum
    t_s = TwoSum()
    nums = [
        [2, 7, 11, 15],
        [3, 2, 4],
        [3, 3]
    ]

    target = [
        9,
        6,
        6
    ]
    print("Two Sum Combination: ")
    solutions = t_s


# run the main file
if __name__ == '__main__':  # this function is used so that only in the main function will be run (not the modules + main())also to make distinctions between files
    main()
