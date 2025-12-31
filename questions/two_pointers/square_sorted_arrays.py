"""
https://leetcode.com/problems/squares-of-a-sorted-array/
"""

"""
Approach:
Step 1: divide the arrays in two array to store positive and negative integers
Case 1.1: If there are no negative numbers, just square the elements of original array and return
Case 1.2: If there are negative numbers, just square the elements of original array, reverse them and return 

Step 2: if there are both positive and negative numbers, First square both the arrays then,
Step 3: Take two pointers i and j pointing both the arrays and then check if 
        pos[i] <= neg[j] then in the resultant array add the pos[i] and move the pointer i+1
Step4: Repeat the above step for negative array as well.

Step 5: If either one of the arrays have remaining elements left to be compared, 
        add those elements to the resultant array.
"""

def solution(nums):
    pos,neg = list(), list()
    i,j=0,0
    res = list()
    for num in nums:
        if num > 0:
            pos.append(num)
        else:
            neg.append(num)

    m,n = len(pos),len(neg)
    print(pos, neg)
    if n == 0:
        return [n*n for n in nums]
    if m == 0:
        return [n*n for n in neg][::-1]

    pos = [n*n for n in pos]
    neg = [n*n for n in neg][::-1]


    while i<m and j<n:
        if pos[i] <= neg[j]:
            res.append(pos[i])
            i+=1
        else:
            res.append(neg[j])
            j+=1

    while i<m:
        res.append(pos[i])
        i+=1

    while j<n:
        res.append(neg[j])
        j+=1

    return res

def main():
    nums = list(map(int, input().split()))
    print(solution(nums))


if __name__ == '__main__':
    main()
