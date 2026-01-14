# Problem:
# Perform linear search to find an element in an array.

# Approach:
# Traverse the array one element at a time
# and compare each element with the target.

# Time Complexity: O(n)
# Space Complexity: O(1)

def linear_search(arr, target):
    for index in range(len(arr)):
        if arr[index] == target:
            return index
    return -1


if __name__ == "__main__":
    data = [10, 20, 30, 40, 50]
    target = 30
    result = linear_search(data, target)
    print("Array:", data)
    print("Target:", target)
    print("Index Found:", result)
