"""
https://leetcode.com/problems/minimum-size-subarray-sum/description/
"""

def sol(nums, k):
    left, sumi = 0,0
    res = float('inf')

    for right in range(len(nums)):
        sumi += nums[right]
        while sumi >= k:
            res = min (right - left + 1, res)
            sumi -= nums[left]
            left+=1
    return res

def main():
    nums = list(map(int, input().split()))
    k = int(input())
    print(sol(nums, k))


if __name__ == '__main__':
    main()
