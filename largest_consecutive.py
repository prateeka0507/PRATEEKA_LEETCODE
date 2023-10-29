def longest_consecutive(nums):
    num_set = set(nums)
    max_length = 0

    for num in nums:
        if num - 1 not in num_set:
            current_num = num
            current_length = 1

            while current_num + 1 in num_set:
                current_num += 1
                current_length += 1

            max_length = max(max_length, current_length)

    return max_length

# Example usage
nums = [100, 4, 200, 1, 3, 2]
result = longest_consecutive(nums)
print(result)
