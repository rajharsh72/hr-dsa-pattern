"""
https://neetcode.io/problems/buy-and-sell-crypto?list=neetcode250
"""

def stock(prices):
    left, right = 0, 1
    maxProfit = 0

    while right < len(prices):
        # checks if buy price is less than sell price
        if prices[left] < prices[right]:
            maxProfit = max(maxProfit, prices[right] - prices[left])
        else:
            left = right
        right += 1
    return maxProfit


def main():
    nums = list(map(int, input().split()))
    print(stock(nums))


if __name__ == '__main__':
    main()
