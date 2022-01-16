from Randomizer import Randomizer

import random
def createPassword(userAnswers, passwordLength):
  TemporaryAnswers = userAnswers.copy()

  randomObj = Randomizer()
  for object in userAnswers:
    object.strip()                                                      #Removes leading and trailing whitespaces
    object.replace(" ", "")                                             #Removes whitespace from within

  #We will mix in the password through multiple layers 
  
  #--This will never change one word twice, as range random.randrange only selects a number between 0 and 3, but in this case just 
  #selecting the number of items to be changed randomly, so regardless, each item will keep is original placement in the list, and therefore
  #we will be able to select what was the original item from based on their placement on the list, etc. Trust.
  
  
  #Pick a random number of words to be selected from 1 to 3
  for i in range(random.randrange(3)):
    diceRoll = random.randint(1,4)
    print("Diceroll = ", diceRoll)
    #Try to apply the anagramFinder and the similarSound
    if (diceRoll == 1):
      print(1)
      TemporaryAnswers[i] = randomObj.findAnagram(userAnswers[i])
    elif (diceRoll == 2):
      print(2)  
      TemporaryAnswers[i] = randomObj.similarSound(userAnswers[i])
    elif (diceRoll ==3):
      print("Numtoletter")
      TemporaryAnswers[i] = randomObj.placeNumber(userAnswers[i])
    else:
      print(4)
      TemporaryAnswers[i] = randomObj.TakeLetterAway(userAnswers[i])
      
      
       
  #Pick a random treatment for each word that was selected
    
  
  
    
  print(userAnswers)
  megaStrPassword = TemporaryAnswers[0] + TemporaryAnswers[1] + TemporaryAnswers[2]    #concatenating all the string responses
  length = len(megaStrPassword)                                         
  index1 = random.randrange(length)
  index2 = random.randrange(length)                                       #Finding 2 random integers to be the range of the slice
  
  if index1<index2:                                                     #Extracting a slice from the mega string
    strPwdSlice = megaStrPassword[index1:index2]
    upper = index1
    lower = index2
  else:
    upper = index2
    lower = index1
    strPwdSlice = megaStrPassword[index2:index1]
  
  password = strPwdSlice
  
  wordMix = []
#Check the upper and lower boundaries with the mega string, and selects the appropiate original word 
  if lower <  len(TemporaryAnswers[0]): #If lower bundary is less than the length of the original word, then that means that the first word was in
    wordMix.append(userAnswers[0])
  elif len(TemporaryAnswers[0])< lower < len(TemporaryAnswers[0]) + len(TemporaryAnswers[1]):   #If lower bound is between the first and second words, that means the second word was in
    wordMix.append(userAnswers[1])
  else:
    wordMix.append(userAnswers[2]) #Otherwise this means that the third word was in 

  if len(userAnswers[0])< upper < len(userAnswers[0]) + len(userAnswers[1]) and userAnswers[1] not in wordMix: #Same logic applies with the upper bound, but in this case
                                                                                                                #we make sure that this is not already in the wordMix
     wordMix.append(userAnswers[1])
  if upper >= len(userAnswers[0]) + len(userAnswers[1]) and userAnswers[2] not in wordMix:
     wordMix.append(userAnswers[2])   
  
  index = random.randint(3,5)                         #Index of the number chosen
  chosennumber = userAnswers[index]                   #Number chosen that is included in the password
  print(password)
  password = chosennumber + password
     
  
  usedchars = []
  charlist = ['~', '@', '#', '$', '%', '^', '&', '*', '(', '(', '-', '+', '[', ']', '{', '}', '|', '<', '>', '/', '?']
  if len(password) < passwordLength:
      currlength = len(password)
  while len(password) < passwordLength:
      random.shuffle(charlist)
      print(1)
      usedchars.append(charlist[0])                       #List of special characters used
      password = password + charlist[0]
  return password
