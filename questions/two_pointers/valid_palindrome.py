"""
    Leetcode: https://leetcode.com/problems/valid-palindrome/description/?envType=problem-list-v2&envId=two-pointers
"""


def solution(s):
    s = s.lower()
    s = "".join(filter(str.isalnum, s))
    print(s)
    left = 0
    right = len(s) -1
    while left < right:
        if s[left] != s[right]:
            return False
        left +=1
        right -=1
    return True

def main():
    s = input()
    print(solution(s))


if __name__ == '__main__':
    main()