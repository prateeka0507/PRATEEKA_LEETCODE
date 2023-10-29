def shortest_palindrome(s):
    n = len(s)
    rev_s = s[::-1]

    for i in range(n):
        if s[:n - i] == rev_s[i:]:
            return rev_s[:i] + s

# Example usage
s = "aacecaaa"
result = shortest_palindrome(s)
print(result)
