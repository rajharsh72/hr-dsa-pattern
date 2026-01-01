"""
Problem: https://leetcode.com/problems/3sum/

Solution Approach:

Step 1: In this problem we will find the 2 sum for every a[i] such that x + y = -a[i]
Step 2: Since we are required to find the unique triplets, we will have to modify the existing 2-sum logic.
Step 3: So whenever we encounter that left + right = target in that case we will increase both the pointers until the current element is not similar to previous pointers
"""


def three_sum(nums):
    nums.sort()
    res = list()
    n = len(nums)
    for i in range (0, n-2):
        # checks for i if current and previous elements are same then skip the iteration as it might result in duplicate values
        if i > 0 and nums[i] == nums[i-1]:
            continue
        left = i+1
        right = n-1
        sumi = -1 * nums[i]
        while left < right:
            curr_sum = nums[left] + nums[right]
            if curr_sum == sumi:
                res.append([nums[i], nums[left], nums[right]])
                left += 1
                right -= 1

                # increase the left pointer until previous and current element are different
                while left < n and nums[left] == nums[left-1]:
                    left += 1
                # decrease the right pointer until previous and current element are different
                while right >= 0 and nums[right] == nums[right+1]:
                    right -= 1

            elif curr_sum < sumi:
                left += 1

            else:
                right -= 1

    return res


def main():
    nums = list(map(int, input().split()))
    print(three_sum(nums))


if __name__ == '__main__':
    main()