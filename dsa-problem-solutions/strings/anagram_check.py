# Problem:
# Check whether two strings are anagrams of each other.

# Approach:
# Sort both strings and compare the results.

# Time Complexity: O(n log n)
# Space Complexity: O(1)

def are_anagrams(str1, str2):
    str1 = str1.replace(" ", "").lower()
    str2 = str2.replace(" ", "").lower()

    return sorted(str1) == sorted(str2)


if __name__ == "__main__":
    string1 = "listen"
    string2 = "silent"
    print("String 1:", string1)
    print("String 2:", string2)
    print("Are Anagrams:", are_anagrams(string1, string2))
