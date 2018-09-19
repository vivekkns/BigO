
def helper(data, k, memo):
    """
    "12345" = "2345" + "345"
    """
    if k == 0:
        return 1

    si = len(data) - k

    if data[si] == '0':
        return 0

    if memo[k] is not None:
        return memo[k]

    num = helper(data, k-1, memo)

    if k > 1 and int(data[si:si+2]) <= 26:
        num += helper(data, k-2, memo)

    memo[k] = num
    return num


def num_ways_top_down(data):
    memo = [None for _ in range(len(data)+1)]
    return helper(data, len(data), memo)


def num_ways_bottom_up(data):
    """
    Fill the table from right to left
    """
    dl = len(data)

    memo = [0 for _ in range(dl + 1)]
    memo[dl] = 1
    if data[dl-1] == '0':
        memo[dl-1] = 0
    else:
        memo[dl-1] = 1

    for si in range(dl-2, -1, -1):
        if data[si] != '0':
            memo[si] = memo[si+1]
            if int(data[si] + data[si+1]) <= 26:
                memo[si] += memo[si+2]
    return memo[0]


if __name__ == '__main__':
    data = "10123"
    print(num_ways_top_down(data))
    print(num_ways_bottom_up(data))