
def fixedSlidingWindow():
    windowSum = 0
    maxi = float('-inf')
    k = 4 #window size
    nums = list()

    #setup initial window
    for i in range(0,k):
        windowSum += nums[i]

    # initialize result
    maxi = windowSum

    # slide from the window accross the array
    for i in range(k,len(nums)):
        windowSum += nums[i] - nums[i - k] # add new element and remove old one
        maxi = max(maxi, windowSum) # update maxiSum or any other computation required

    return maxi


def striverSlidingWindowFixeed():
    maxi = float('-inf')
    k = 4 #window size
    left, right = 0, k-1
    nums = list()
    sumi = 0
    for i in range(0,k):
        sumi += nums[i]
    maxi = sumi

    while right < k-1:
        sumi -= nums[left]
        left+=1
        right+=1
        sumi += nums[right]

        maxi = max(maxi, sumi)

    return maxi




"""
used for finding the longest or shortest subarray/substring that satisfies the given condition
"""

def dyanmicSlidingWindow(nums):
    left, windowSum = 0, 0
    maxi = float('-inf')
    nums = list()

    for right in range(len(nums)):
        ab = 1
        # update the windowSum to include nums[right] -- to expand the window
        #while windowSum violates the condition
            #update maxiSum -- if needed
            #update windowSum to exclude nums[left] -- shrink the window
            #move left pointer forward
    return maxi
