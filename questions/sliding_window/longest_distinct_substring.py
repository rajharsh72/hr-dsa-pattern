"""
https://leetcode.com/problems/longest-substring-without-repeating-characters/description/
"""


def sol(s):
    left = 0
    visited = set()
    res = 0

    for right in range(len(s)):

        while s[right] in visited:
            visited.remove(s[left])
            left +=1

        visited.add(s[right])
        res = max(res, right - left + 1)

    return res