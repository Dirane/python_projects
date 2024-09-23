def first_non_repeat_char(s):
    char_count = {}

    # Count frequency of each character
    for char in s:
        char_count[char] = char_count.get(char, 0) + 1

    for char in s:
        if char_count[char] == 1:
            return char

    return None

# Exanple usage
print(first_non_repeat_char("leetcode")) 
print(first_non_repeat_char("aabbcc"))