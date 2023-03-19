def schedule_intervals(intervals):
    intervals.sort(key=lambda x: x[1])  # sort intervals by end time
    count = 0
    end_time = -float('inf')
    for interval in intervals:
        if interval[0] >= end_time:
            count += 1
            end_time = interval[1]
    return count

# read input
num_instances = int(input())
for _ in range(num_instances):
    num_jobs = int(input())
    intervals = []
    for _ in range(num_jobs):
        start, end = map(int, input().split())
        intervals.append((start, end))
    print(schedule_intervals(intervals))
