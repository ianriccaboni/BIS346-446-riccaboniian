import numpy as np
import statistics as stats

responses = [1, 2, 5, 4, 3, 5, 2, 1, 3, 3, 1, 4, 3, 3, 3, 2, 3, 3, 2, 5]
values, counts = np.unique(responses, return_counts=True)
values = list(values)
counts = list(counts)

print('Reponses and frequencies:')
for value, count in zip(values, counts):
    print(f'{value}: {count}')

print(f'Fewest Responses: {values[counts.index(min(counts))]} occurred {min(counts)} time(s)')
print(f'Most Responses: {values[counts.index(max(counts))]} occurred {max(counts)} time(s)')
print(f'Range of response totals: {min(counts)}-{max(counts)}')
print(f'Mean response count: {stats.mean(counts)}')
print(f'Median response count: {stats.mean(counts)}')
print(f'Mode response count: {stats.mode(counts)}')
print(f'Variance: {stats.pvariance(counts)}')
print(f'Standard deviation: {stats.pstdev(counts)}')