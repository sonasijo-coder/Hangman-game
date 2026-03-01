import random
words = ["Pyhton","Django","Hangman","Developer","Computer"]
word=random.choice(words)
guessed_letters=[]
tries=6
print("Welcome to Hangamn Game")
while tries>0:
  display_word=""
  for letter in word:
    if letter in guessed_letters:
      display_word += letter + ""
    else:
      display_word += "_"
  print("\nWord:", display_word)
  print("Tries left:",tries)
  guess = input("Guess a letter:").lower()
  if guess in word:
    print(" correct guess!")
    guessed_letters.append(guess)
  else:
    print("Wrobg Guess")
    tries-=1
  if all(letter in guessed_letters for letter in word):
     print("\n Congratulations! You gussed the word:", word)
     break
else:
  print("\n Game Over ! The word was:", word)