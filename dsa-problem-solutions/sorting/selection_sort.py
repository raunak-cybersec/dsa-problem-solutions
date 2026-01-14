# Problem:
# Sort an array using Selection Sort.

# Approach:
# Repeatedly find the minimum element from
# the unsorted part and place it at the beginning.

# Time Complexity: O(n^2)
# Space Complexity: O(1)

def selection_sort(arr):
    n = len(arr)

    for i in range(n):
        min_index = i
        for j in range(i + 1, n):
            if arr[j] < arr[min_index]:
                min_index = j

        arr[i], arr[min_index] = arr[min_index], arr[i]

    return arr


if __name__ == "__main__":
    data = [29, 10, 14, 37, 13]
    print("Original:", data)
    print("Sorted:", selection_sort(data))
