from Easy.Height_Checker import Height_Checker  # import module the height checker function from height checker file
from Medium.Permutations import Permutations    # import module permutation function from permutation file

def main():
    # method to callout the function so it will be called later in the loop
    hc = Height_Checker()
    # leetcode question   
    height_list = [     
        [1,1,4,2,1,3], 
        [5,1,2,3,4], 
        [1,2,3,4,5]
    ]
    # loop the lists and print the result
    for heights in height_list:
        print('Height Checker Results:', hc.heightChecker(heights))

    # method to callout the function so it will be called later in the loop
    perm = Permutations()
    # leetcode question
    nums_list = [
        [1,2,3], 
        [0,1],
        [1]
    ]
    # loop the list and print the result
    for nums in nums_list:
        print('Permutation Results: ', perm.permute(nums))

# run the main file
if __name__ == '__main__':  # this function is used so that only in the main function will be run (not the modules + main())also to make distinctions between files
    main()
