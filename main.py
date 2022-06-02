x = input("Enter Some Statement: ")
characterCount = 0
wordCount = 1
for i in x:
    characterCount = characterCount + 1
    if i == ' ':
        wordCount = wordCount + 1
print("Number Of Words In The Statement: ")
print(wordCount)
print("Number Of Characters In The Statement: ")
print(characterCount)
