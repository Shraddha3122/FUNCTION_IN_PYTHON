# Create a function to count the number of vowels and consonants in a string.


def count_vowels_and_consonants(s):
    # Define vowels
    vowels = "aeiouAEIOU"
    # Initialize counters
    vowel_count = 0
    consonant_count = 0

    # Iterate through each character in the string
    for char in s:
        if char.isalpha():  # Check if the character is a letter
            if char in vowels:
                vowel_count += 1
            else:
                consonant_count += 1

    return vowel_count, consonant_count

input_string = "Hello, World!"
vowels, consonants = count_vowels_and_consonants(input_string)
print(f"Vowels: {vowels}, Consonants: {consonants}")