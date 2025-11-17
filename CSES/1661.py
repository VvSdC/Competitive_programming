import sys
import random

RANDOM = random.randrange(2**62)

def hash_wrapper(x):
    return x^RANDOM

def subarray_sums2():
    # Taking input of n and x
    n,x = map(int,input().split())

    # Taking list input
    arr = list(map(int,input().split()))

    current_sum = 0
    mp = {hash_wrapper(0):1}
    total_subarrays = 0

    for number in arr:
        current_sum += number

        key = hash_wrapper(current_sum - x)
        if key in mp:
            total_subarrays += mp[key]

        key = hash_wrapper(current_sum)
        if key in mp:
            mp[key] += 1
        else:
            mp[key] = 1

    print(total_subarrays)

if __name__ == "__main__":
    subarray_sums2()