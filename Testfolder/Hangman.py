import random
print("Hi! Welcome to hangman sea edition! The secret word is related to the sea.")
def get_guess():
    #set amount of dashes when starting (depending on the word givens)
  dashes = "-" * len(secret_word)
  guesses_left = 10
#each time player guesses the wrong letter, elimate a life
#the number of guesses left will always be more than -1
  while guesses_left > -1 and not dashes == secret_word:
    print(dashes)
    print (str(guesses_left))
    guess = input("Guess:")
    #condition if guess imput is not a single letter
    if len(guess) != 1:
      print ("Your guess must have exactly one letter! NO MORE THAN ONE CHARACTER!")
      #if the correct letter is guessed, the letter will replace the dash
    elif guess in secret_word:
      print ("You are one step closer to solving the secret word!")
      dashes = update_dashes(secret_word, dashes, guess)
    else:
      print ("That letter is not in the secret word!")
      guesses_left -= 1
  if guesses_left < 0:
    print ("You lose. The word was: " + str(secret_word))
      # If the dash string equals the secret word in the end then the user wins
  else:
    print ("Congrats! You figured it out! The word was: " + str(secret_word))
    print("Thanks for playing :)")
    #updates string of dashes with updated charcters guessed correct
def update_dashes(secret, cur_dash, rec_guess):
  result = ""
  for i in range(len(secret)):
      #if guessed correctly another guess is added to the string
    if secret[i] == rec_guess:
        #records guess if correct
      result = result + rec_guess
    else:
      result = result + cur_dash[i]
  return result
  #word bank provided for random generator
words = ["dolphin", "wave", "swimming", "whale", "seahorse", "coral", "fish", "turtle", "snorkeling"]
#random word chosen to guess for player
secret_word = random.choice(words)
get_guess()
