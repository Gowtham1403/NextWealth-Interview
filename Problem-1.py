'''
Problem 1:
Read a passage from a file. (If you don't know how to handle files in Python, you can hardcode a long passage)
Count the number of times the word 'the' followed by another 'the' without 'a' in between.

Eg The king went to the forest with the wife and a servernt. The king shot a deer. The king went to the forest again the next day.

answer is 4 (The king, the forest, The King the next).
'''

passage = "The king went to the forest with the wife and a servernt. The king shot a deer. The king went to the forest again the next day."

words = passage.split()

count = 0

for i in range(len(words) - 3):
    if words[i].lower() == 'the' and words[i + 1].lower() != 'a' and words[i + 3].lower() == 'the':
            count += 1

print("The count of the is:", count)