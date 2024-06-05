def find_first_repeating_character(s):
    char_count = {}
    
    for char in s:
        if char in char_count:
            print(f"First repeating character: {char}, Memory address: {id(char)}")
            return char, id(char)
        else:
            char_count[char] = 1
    
    return None

# Example usage
result = find_first_repeating_character(input("Enter your word: "))
if result:
    character, memory_address = result
else:
    print("No repeating character found.")
