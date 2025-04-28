a = [5, 8, 7, 9, 10, 2]

max_sum = a[0] + a[1]
max_pair = (a[0], a[1])

for i in range(1, len(a) - 1):  # Loop until second last index
    current_pair = (a[i], a[i + 1])
    current_sum = a[i] + a[i + 1]

    print(f"Pair: {current_pair}, Sum: {current_sum}")

    if current_sum > max_sum:
        max_sum = current_sum
        max_pair = current_pair

print(f"\nThe highest sum of adjacent pairs is: {max_sum}, from the pair: {max_pair}")
