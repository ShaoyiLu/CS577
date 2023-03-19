from typing import List, Tuple

def weighted_interval_scheduling(jobs: List[Tuple[int, int, int]]) -> int:
    # sort jobs by finish time
    jobs.sort(key=lambda x: x[1])

    n = len(jobs)
    dp = [0] * n
    dp[0] = jobs[0][2]

    for i in range(1, n):
        # find the latest job that doesn't conflict with the current job
        j = i - 1
        while j >= 0 and jobs[j][1] > jobs[i][0]:
            j -= 1

        # include the current job or not
        include = jobs[i][2]
        if j >= 0:
            include += dp[j]

        dp[i] = max(include, dp[i - 1])

    return dp[-1]


if __name__ == '__main__':
    num_tests = int(input())
    for _ in range(num_tests):
        n = int(input())
        jobs = []
        for _ in range(n):
            i, j, k = map(int, input().split())
            jobs.append((i, j, k))
        print(weighted_interval_scheduling(jobs))
