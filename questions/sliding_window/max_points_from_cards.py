"""
https://leetcode.com/problems/maximum-points-you-can-obtain-from-cards/description/
"""

def max_points_from_cards(cards, k):
    leftSum = rightSum = maxSum = 0
    rightIndex = len(cards) - 1
    for i in range(0,k):
        leftSum += cards[i]
    maxSum = leftSum

    for i in range(k-1, -1,-1):
        leftSum -= cards[i]
        rightSum += cards[rightIndex]
        rightIndex -= 1
        maxSum = max(maxSum, rightSum + leftSum)
    return maxSum



def main():
    cards = list(map(int, input().split()))
    k = int(input())
    print(max_points_from_cards(cards, k))


if __name__ == '__main__':
    main()
