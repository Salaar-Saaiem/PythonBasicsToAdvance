# Problem:
# Take a sentence from the user and perform the following operations:
#
# 1. Count total words
# 2. Count total characters (excluding spaces)
# 3. Find the longest word
# 4. Count how many times a specific character appears
# 5. Print words starting with a vowel
# 6. Convert first letter of every word into uppercase

text = input("Enter a sentence: ")
character = input("Enter a character to count: ")


# 1 - Counting Words in a Sentance
word1=text.split()
print(f"Total No. of Words in Sentance is {len(word1)}")


# 2 - Count Total characters Excluding Spaces
char_count=0
for i in text:
    if i != ' ':
        char_count+=1
print('Total No. of Character in string is: ',char_count)


# 3 -Find the Largest word
largest_word=''
splitted = text.split()
for word in splitted:
    if len(word) > len(largest_word):
        largest_word = word
print('Largest word in the sentance is: ',largest_word)
'''#another 
split_list= text.split()
largest_word= max(split_list, key=len) #max function takes the list and key is the length of the word, it will return the largest word in the list
print(largest_word)'''


# 4 - Count how many times a specific character appears
count = 0 
for i in text:
    if i == character:
        count +=1
print(f"The character '{character}' appears {count} times in the sentence.")
'''### another
count = text.count(character)
print(count)
###'''

# 5 - Print words starting with a vowel
vowels='aeiouAEIOU'
for word in text.split():
    if word[0] in vowels:
        print(word)

# 6 - Convert first letter of every word into uppercase
print(text.title())
