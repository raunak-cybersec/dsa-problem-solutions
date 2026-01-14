# Problem:
# Perform binary search on a sorted array.

# Approach:
# Repeatedly divide the search interval in half
# based on comparison with the middle element.

# Time Complexity: O(log n)
# Space Complexity: O(1)

def binary_search(arr, target):
    left = 0
    right = len(arr) - 1

    while left <= right:
        mid = (left + right) // 2

        if arr[mid] == target:
            return mid
        elif arr[mid] < target:
            left = mid + 1
        else:
            right = mid - 1

    return -1


if __name__ == "__main__":
    data = [5, 10, 15, 20, 25]
    target = 15
    result = binary_search(data, target)
    print("Array:", data)
    print("Target:", target)
    print("Index Found:", result)
