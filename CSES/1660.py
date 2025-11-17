import random

RANDOM = random.randrange(2**60)

def hash_wrapper(x):
    return x ^ RANDOM

def subarray_sum1():
    # Taking input of n and x
    n,x = map(int,input().split())
    
    # Taking array input
    arr = list(map(int,input().split()))

    # Taking dictionary to store sums
    current_sum = 0
    mp = {hash_wrapper(0):1}
    total_sub_arrays = 0

    for number in arr:
        current_sum += number

        #Checking is sub-array of sum x exists
        key = hash_wrapper(current_sum - x)
        if key in mp:
            total_sub_arrays += mp[key]

        # Storing the current sum
        key = hash_wrapper(current_sum)
        if key in mp:
            mp[key] += 1
        else:
            mp[key] = 1
    
    print(total_sub_arrays)


if __name__ == "__main__":
    subarray_sum1()
