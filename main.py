import random
import os
import time

print("Welcome to Hangman game")
listOfWords = ["demon","adorable","heavenly","lovely","witty", "intelligent", "clever","kind", "talented","courageous", "brave","beautiful","daring","charming","ambitious"]
letterPicked = []
lives = 11
word = random.choice(listOfWords)
print(word)
while True:
  time.sleep(2)
  os.system("clear")
  letter = input("Choose a letter : ").lower()
  if letter in letterPicked:
    print("You have already tried this letter before!")
    continue
  letterPicked.append(letter) 
  if letter in word:
    print("You found a letter!")
  else:
    print("No, this letter is not in the word!You lose a life!")
    lives -= 1
  allLetters = True
  print()
        
  for i in word :
    if i in letterPicked:
      print(i, end = "")
    else:
      print("_", end = "")
      allLetters = False
  print()
  if allLetters:
    print("You won with", lives,"left!")
    break
  if lives <= 0:
    print("You are out of lives already! The correct answer is ", word)
    break
  else:
    print("Only", lives, "left!,keep trying some more!")
      
  
    
  


  
  
      



    

