with open('day3.input') as f:
    binary_strings = f.read().splitlines()

number_of_ones = [0]*len(binary_strings[0])
total_entries = len(binary_strings)

for bin_str in binary_strings:
    for i,c in enumerate(bin_str):
        if c == '1':
            number_of_ones[i] += 1

# pylint: disable=invalid-name
gamma_rate = str.join("", ["1" if num >= total_entries / 2 else "0" for num in number_of_ones])
epsilon_rate = str.join("", ["0" if char == "1" else "1" for char in gamma_rate])

gamma_rate = int(gamma_rate, 2)
epsilon_rate = int(epsilon_rate, 2)
# pylint: enable=invalid-name

print(gamma_rate * epsilon_rate)
