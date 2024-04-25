from Easy.Height_Checker import Height_Checker
from Medium.Permutations import Permutations

def main():
    hc = Height_Checker()
    height_list = [
        [1,1,4,2,1,3], 
        [5,1,2,3,4], 
        [1,2,3,4,5]
    ]
    for heights in height_list:
        print('Height Checker Results:', hc.solve(heights))

    perm = Permutations()
    nums_list = [
        [1,2,3], 
        [0,1],
        [1]
    ]
    for nums in nums_list
    print('Permutation Results: ', perm.solve(nums))

if __name__ == '__main__':
    main()
