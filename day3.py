# pylint: disable=invalid-name

with open('day3.input') as f:
    binary_strings = f.read().splitlines()

def most_common_bit(binary_string_list, bit_index, tie_winner): # pylint: disable=missing-function-docstring
    total_entries = len(binary_string_list)
    number_of_ones = 0
    for entry in binary_string_list:
        if entry[bit_index] == "1":
            number_of_ones += 1
    if number_of_ones > total_entries / 2:
        return "1"
    if number_of_ones < total_entries / 2:
        return "0"
    return tie_winner

gamma_rate = ""
epsilon_rate = ""

for i,_ in enumerate(binary_strings[0]):
    if most_common_bit(binary_strings, i, "1") == "1":
        gamma_rate += "1"
        epsilon_rate += "0"
    else:
        gamma_rate += "0"
        epsilon_rate += "1"

gamma_rate = int(gamma_rate, 2)
epsilon_rate = int(epsilon_rate, 2)

print(gamma_rate * epsilon_rate)

oxygen_numbers = list(binary_strings)
current_bit_index = 0
while len(oxygen_numbers) > 1:
    common_bit = most_common_bit(oxygen_numbers, current_bit_index, "1")
    oxygen_numbers = [x for x in oxygen_numbers if x[current_bit_index] == common_bit]
    current_bit_index += 1
oxygen_generator_rate = int(oxygen_numbers[0], 2)

co2_numbers = list(binary_strings)
current_bit_index = 0
while len(co2_numbers) > 1:
    common_bit = most_common_bit(co2_numbers, current_bit_index, "1")
    common_bit = "1" if common_bit == "0" else "0"
    co2_numbers = [x for x in co2_numbers if x[current_bit_index] == common_bit]
    current_bit_index += 1
co2_scrubber_rate = int(co2_numbers[0], 2)

print(oxygen_generator_rate * co2_scrubber_rate)
