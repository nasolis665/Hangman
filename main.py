import random
num_lives=6
word_list=("abruptly", "absurd", "abyss", "affix", "asked", "avenue", "awkward", "axiom", "azure", "bagpipes", "bandwagon", "banjo", "bayou", "beekeeper", "bikini", "blitz", "blizzard", "boggle", "bookworm", "boxcar", "boxful", "buckaroo", "buffalo", "buffoon", "buxom", "buzzard")
word=random.choice(word_list)
word_letters=list(word)
print(word_letters) ##uncomment if you wanna cheat##
letters_found=[]
print("Hello we are playing a game of hang man I'm thinking of a word and you gotta pick it")
while num_lives != 0:
  letter=input("what letter do you want to guess?")
  letter=letter.lower()
  if letter in word_letters:
    print("You got a letter!")
    letters_found.append(letter)
    word_letters.remove(letter)
    length=len(word_letters)
    if length == 0:
      print("You Win!")
      break
  elif letter not in word_letters:
    print("You did not get a letter")
    num_lives -= 1
    print(f"You have {num_lives} lives")
if num_lives == 0:
  print("You Lose")
  print(f"you found these letters: {letters_found}, the word was {word}")
