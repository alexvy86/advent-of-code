window_size = 3
num_of_increases = 0

measurements = []
with open('day1.input') as f:
    measurements = [int(line) for line in f]

for i in range(0,len(measurements) - window_size):
    prev_window_sum = sum(measurements[i:i+window_size])
    current_window_sum = sum(measurements[i+1:i+1+window_size])
    if current_window_sum > prev_window_sum:
        num_of_increases += 1

print(num_of_increases)
