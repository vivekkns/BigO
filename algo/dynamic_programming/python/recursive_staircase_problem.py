
# if steps are [1, 2] then, it is like computing fibonacci number


def num_ways(N, steps):
    if N == 0:
        return 1
    total_steps = 0
    for step in steps:
        if (N - step) >= 0:
            total_steps += num_ways(N-step, steps)
    return total_steps


def num_ways_bottom_up(N, steps):
    if N == 0:
        return 1
    nums = [0] * (N+1)
    nums[0] = 1
    for n in range(1, N+1):
        for step in steps:
            if n-step >= 0:
                nums[n] += nums[n-step]
    return nums[N]

if __name__ == '__main__':
    N = 2
    step_options = [1, 2]
    print(N, step_options, num_ways(N, step_options))
    print(N, step_options, num_ways_bottom_up(N, step_options))

    N = 10
    step_options = [1, 3, 5]
    print(N, step_options, num_ways_bottom_up(N, step_options))
