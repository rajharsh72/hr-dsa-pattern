"""
Leetcode: https://leetcode.com/problems/sort-colors/description/
"""

def sort_colors(nums):
    low , mid = 0,0
    high = len(nums)-1

    while mid <= high:
        if nums[mid] == 0:
            nums[low], nums[mid] = nums[mid], nums[low]
            low += 1
            mid += 1

        elif nums[mid] == 1:
            mid +=1

        elif nums[mid] == 2:
            nums[mid], nums[high] = nums[high], nums[mid]
            high -= 1

    return nums


def main():
    nums = list(map(int, input().split()))
    print(sort_colors(nums))


if __name__ == '__main__':
    main()