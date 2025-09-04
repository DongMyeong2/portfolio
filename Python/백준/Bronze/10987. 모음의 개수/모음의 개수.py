vowel ="aeiou"
word = list(input())
count = 0
for i in range(len(word)):
  if word[i] in vowel:
    count+=1
print(count)