# Problem:
# Take a sentence from the user and perform the following operations:
#
# 1. Print the frequency of each character
# 2. Find the most repeated character
# 3. Remove duplicate characters
# 4. Count total vowels and consonants
# 5. Print characters occurring more than once
# 6. Replace vowels with '*'

text = input("Enter a sentence: ")


# 1. Print the frequency of each character
char_freq = {}
for char in text:
    if char in char_freq:
        char_freq[char] += 1
    else:
        char_freq[char] = 1 
print("Character Frequency:", char_freq)


# 2. Find the most repeated character

# 3. Remove duplicate characters
# 4. Count total vowels and consonants
# 5. Print characters occurring more than once
# 6. Replace vowels with '*'