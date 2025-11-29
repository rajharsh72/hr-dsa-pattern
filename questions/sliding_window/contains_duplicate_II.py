"""
https://leetcode.com/problems/contains-duplicate-ii/description/?envType=problem-list-v2&envId=sliding-window
"""


def contains_duplicate(nums, k):
    left, right = 0, 0
    visited = set()

    while right < len(nums):
        if nums[right] in visited:
            return True
        visited.add(nums[right])
        right += 1
        if right - left > k:
            visited.remove(nums[left])
            left += 1
    return False


def main():
    nums = list(map(int, input().split()))
    k = int(input())
    print(contains_duplicate(nums, k))


if __name__ == '__main__':
    main()
