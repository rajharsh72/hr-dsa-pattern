
def longest_subarray_sum(arr, k):
    l,r,maxLen,sumi=0,0,0,0

    while r<len(arr):
        sumi += arr[r]
        if sumi > k:
            sumi -= arr[l]
            l+=1
        if sumi <= k:
            maxLen = max(maxLen, r-l+1)
        r+=1

    return maxLen

def main():
    arr=[1,2,3,4,5,6,7,8,9,10,11,12,13,14,15]
    k=3
    print(longest_subarray_sum(arr,k))

if __name__ == '__main__':
    main()
