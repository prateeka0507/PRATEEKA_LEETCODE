def is_additive_number(s):
    def is_valid(num1, num2, remaining):
        if not remaining:
            return True
        sum_str = str(int(num1) + int(num2))
        if remaining.startswith(sum_str):
            return is_valid(num2, sum_str, remaining[len(sum_str):])
        return False

    n = len(s)
    for i in range(1, n):
        for j in range(i+1, n):
            num1, num2 = s[:i], s[i:j]
            remaining = s[j:]
            if num1.startswith('0') and len(num1) > 1 or num2.startswith('0') and len(num2) > 1:
                continue
            if is_valid(num1, num2, remaining):
                return True
    return False

print(is_additive_number("112358"))
print(is_additive_number("199100199"))
print(is_additive_number("1023"))
## time complexity->O(N^3)
## space complexity->O(N)
