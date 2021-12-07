WINDOW_SIZE = 3
num_of_increases = 0 # pylint: disable=invalid-name

measurements = []
with open('day1.input') as f:
    measurements = [int(line) for line in f]

for i in range(0,len(measurements) - WINDOW_SIZE):
    prev_window_sum = sum(measurements[i:i+WINDOW_SIZE])
    current_window_sum = sum(measurements[i+1:i+1+WINDOW_SIZE])
    if current_window_sum > prev_window_sum:
        num_of_increases += 1

print(num_of_increases)
