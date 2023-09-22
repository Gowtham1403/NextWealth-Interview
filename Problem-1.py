def count_the_followed_by_the(passage):
 
  words = passage.lower().split()

  count = 0
  for i in range(len(words) - 3):
    if words[i].lower() == 'the' and words[i + 1].lower() != 'a':
        if  words[i + 3].lower() == 'the':
            count += 1

  return count

# Example
passage = "The king went to the forest with the wife and a servant. The king shot a deer. The king went to the forest again the next day."
result = count_the_followed_by_the(passage)
print(result)  