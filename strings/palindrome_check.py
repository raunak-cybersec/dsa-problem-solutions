# Problem:
# Check whether a given string is a palindrome.

# Approach:
# Compare characters from the start and end of the string.
# Ignore case differences.

# Time Complexity: O(n)
# Space Complexity: O(1)

def is_palindrome(s):
    s = s.lower()
    left = 0
    right = len(s) - 1

    while left < right:
        if s[left] != s[right]:
            return False
        left += 1
        right -= 1

    return True


if __name__ == "__main__":
    test_string = "Madam"
    print("String:", test_string)
    print("Is Palindrome:", is_palindrome(test_string))
