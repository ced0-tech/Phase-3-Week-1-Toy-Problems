def solve(s):
    consonants = "bcdfghjklmnpqrstvwxyz"
    max_value = 0
    current_value = 0
    
    for char in s:
        if char in consonants:
            current_value += ord(char) - ord('a') + 1
        else:
            max_value = max(max_value, current_value)
            current_value = 0
    
    max_value = max(max_value, current_value)
    
    return max_value