def static_sum_query():
    # Taking n and q as input
    n,q = map(int, input().split())

    # Taking the array input
    arr = list(map(int, input().split()))

    # Taking the queries list
    queries = [tuple(map(int,input().split())) for index in range(q)]

    # Creating the prefix sum array
    prefix_sum = [0]*(n+1)

    for i in range(n):
        prefix_sum[i+1] = prefix_sum[i] + arr[i]

    # Processing each query
    for l,r in queries:
        print(prefix_sum[r]-prefix_sum[l-1])


if __name__ == "__main__":
    static_sum_query()