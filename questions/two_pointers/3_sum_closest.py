"""
Problem: https://leetcode.com/problems/3sum-closest/description/

Solution Approach:

Step 1: In this problem we will find the 2 sum for every a[i]
Step 2: In the 2 sum logic we will check if the current absolute difference is the minimum then that will be your result and the sum will be returned
"""


def three_sum(nums, target):
    nums.sort()
    res = 0
    max_diff = float('inf')
    n = len(nums)
    for i in range (0, n-2):
        left = i+1
        right = n-1
        while left < right:
            curr_sum = nums[i] + nums[left] + nums[right]
            curr_diff = abs(target - curr_sum)

            if curr_diff < max_diff:
                max_diff = curr_diff
                res = curr_sum

            if curr_sum == target:
                left += 1
                right -= 1

            elif curr_sum < target:
                left += 1

            else:
                right -= 1

    return res


def main():
    nums = list(map(int, input().split()))
    target = int(input())
    print(three_sum(nums, target))


if __name__ == '__main__':
    main()