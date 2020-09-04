import time

import random



while True:

  Q = input(">").rstrip().lower()


  jokes = []
  jokes.append(['What did the skeleton say when he got spooked?', 'He was chilled to the bone!'])
  jokes.append(["Why do archeologists keep dinosuar bones on their car?", "Because they're fossil fuels!"])
  jokes.append(["Why did the dog cross the road?", "To get to the barking lot!"])
  jokes.append(["what did the bread think when the dragon attacked?", "'I'm toast"])
  jokes.append(["A Englishman and a Scotsman walk into a bar.", "The Irishman says:'ay laddy, that has got to hurt.'"])
  jokes.append(["You know all those graveyards? They're really popular nowadays.", "Cause everyones dying to get in!"])
  jokes.append(["What is the duck knight called?", "Sir Quack-a-lot!"])
  jokes.append(["Which type of donut is homer simpsons favorite?", "A doh!nut"])
  jokes.append(["two scientests walked into a bar, one ordered H20, the other said 'I'll have H20 too!", "The second scientest died."])
  jokes.append(["A chicken layed more eggs than usual, and what did the farmer say?", "Eggcellent."])
  jokes.append(["A man ate chicken in front of a Emu.", "It was not emused."])
  jokes.append(["Why were the FBI worried about the spaghetti?", "It looked like a impasta."])
  jokes.append(["What do you call a cat destroying the house?", "A catastrophe! And hundreds of dollars in damages."])

  oops = []
  oops.append("My proccessers cannot compute that.")
  oops.append("I'm afraid my language proccessers cannot tell what you said.")
  oops.append("My logic calculators do not make sense of that.")
  oops.append("Error, Error")
  oops.append("Pardon me, I don't understand.")
  oops.append("Huh? I can't seem to find a response.")

  if Q == "Hello".lower() or Q == "Hi".lower():
    print("Hi!")

  elif Q == "What are you".lower() or Q == "Who are you".lower() or Q == "Who are you?".lower() or Q == "What are you?".lower():
    print("I am Robby! Do you want to know what I can do?")

  elif Q == "What can you do?".lower() or Q == "What can you do".lower():
    print("I tell jokes! Would you like to hear one?")

  #if Q == "Yes".lower():
  #  rnd_joke = random.choice(jokes)
  #  print(rnd_joke[0])
  #  time.sleep(3)
  #  print(rnd_joke[1])
      
  #elif Q != "Yes".lower():
  #  pass

  elif Q == "Tell me a joke".lower(): 
    rnd_joke = random.choice(jokes)
    print(rnd_joke[0])
    time.sleep(3)
    print(rnd_joke[1])

  elif Q == "bye":
    break
  
  else :
    print(random.choice(oops))

