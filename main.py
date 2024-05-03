from Easy.Height_Checker import Height_Checker  # import module the height checker function from height checker file
from Medium.Permutations import Permutations    # import module permutation function from permutation file
from Medium.CombinationSum import CombSum

def main():
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

    # combSum = CombSum()
    # candidate_list = [
    #     [2,3,6,7],
    #     [2,3,5],
    #     [2]
    # ]
    # targets = [7, 8, 1]
    # print('Combination Sum: ')
    # for candidates, target in zip(candidate_list,targets):
    #     print(f'For candidates {candidates} with target {target}')
    #     result = (combSum.combinationSum(candidates, target))
    #     print(result)
# run the main file
if __name__ == '__main__':  # this function is used so that only in the main function will be run (not the modules + main())also to make distinctions between files
    main()
