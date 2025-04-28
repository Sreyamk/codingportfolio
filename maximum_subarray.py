def maxim_subarray(arr):
    sum = 0
    maxi = arr[0]
    start = end = s = 0  # Track indices for the subarray

    for i in range(0, len(arr)):
        sum += arr[i]

        if sum > maxi:
            maxi = sum
            start = s
            end = i

        if sum < 0:
            sum = 0
            s = i + 1  # Potential new start of subarray

    return maxi, arr[start:end+1]

# Example usage
arr = [-2, 1, -3, 4, -1, 2, 1, -5, 4]
max_sum, subarray = maxim_subarray(arr)
print("Maximum subarray sum is:", max_sum)
print("Maximum subarray is:", subarray)
