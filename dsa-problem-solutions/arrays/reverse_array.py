# Problem:
# Reverse an array of integers.

# Approach:
# Use two pointers starting from both ends of the array.
# Swap elements until the pointers meet.

# Time Complexity: O(n)
# Space Complexity: O(1)

def reverse_array(arr):
    left = 0
    right = len(arr) - 1

    while left < right:
        arr[left], arr[right] = arr[right], arr[left]
        left += 1
        right -= 1

    return arr


if __name__ == "__main__":
    sample_array = [1, 2, 3, 4, 5]
    print("Original:", sample_array)
    print("Reversed:", reverse_array(sample_array))
