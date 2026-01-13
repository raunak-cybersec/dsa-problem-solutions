# Problem:
# Find the maximum and minimum element in an array.

# Approach:
# Traverse the array once and keep updating
# the maximum and minimum values.

# Time Complexity: O(n)
# Space Complexity: O(1)

def find_max_min(arr):
    if not arr:
        return None, None

    maximum = arr[0]
    minimum = arr[0]

    for element in arr:
        if element > maximum:
            maximum = element
        if element < minimum:
            minimum = element

    return maximum, minimum


if __name__ == "__main__":
    sample_array = [7, 2, 9, 4, 1]
    max_val, min_val = find_max_min(sample_array)
    print("Array:", sample_array)
    print("Maximum:", max_val)
    print("Minimum:", min_val)
