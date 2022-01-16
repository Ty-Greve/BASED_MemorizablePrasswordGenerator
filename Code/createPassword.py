from Randomizer.py import Randomizer

def createPassword(userAnswers, passwordLength):
  randomObj = Randomizer()
  for object in userAnswers:
    object.strip()                                                      #Removes leading and trailing whitespaces
    object.replace(" ", "")                                             #Removes whitespace from within

  ORIGINALANSWERS = userAnswers.copy()
  #We will mix in the password through multiple layers 
  randomTreatment = [userAnswers[0], userAnswers[1], userAnswers[3]]
  random.shuffle(randomTreatment)
  
  #--This will never change one word twice, as range random.randrange only selects a number between 0 and 3, but in this case just 
  #selecting the number of items to be changed randomly, so regardless, each item will keep is original placement in the list, and therefore
  #we will be able to select what was the original item from based on their placement on the list, etc. Trust.
  
  
  #Pick a random number of words to be selected from 1 to 3
  for i in range(random.randrange(3))
    diceRoll = random.randint(1,4)
    #Try to apply the anagramFinder and the similarSound
    if (diceRoll == 1):
      userTreatment[i] = randomObj.anagramFinder(userTreatment[i])
    elif (diceRoll == 2):
      userTreatment[i] = randomObj.similarSound(userTreatment[i])
    elif (diceRoll ==3):
      userTreatment[i] = randomObj.LetterToNumber(userTreatment[i])
    else:
      userTreatment[i] = randomObj.TakeLetterWay(userTreatment[i])
      
      
       
  #Pick a random treatment for each word that was selected
    
  
  
    
  
  megaStrPassword = userAnswers[0] + userAnswers[1] + userAnswers[2]    #concatenating all the string responses
  length = len(megaStrPassword)                                         
  index1 = random.randint(length)
  index2 = random.randint(length)                                       #Finding 2 random integers to be the range of the slice
  
  if index1<index2:                                                     #Extracting a slice from the mega string
    strPwdSlice = megaStrPassword[index1:index2]
    upper = index1
    lower = index2
  else
    upper = index2
    lower = index1
    strPwdSlice = megaStrPassword[index2:index1]
  
  password = strPwdSlice
  
  wordMix = []
#Check the upper and lower boundaries with the mega string, and selects the appropiate original word 
  if lower <  len(userAnswers[0]): #If lower bundary is less than the length of the original word, then that means that the first word was in
    wordMix.append(ORIGINALANSWERS[0])
  elif len(usersAnswers[0])< lower < len(userAnswers[0] + len(userAnswers[1]): #If lower bound is between the first and second words, that means the second word was in
    wordMix.append(ORIGINALANSWERS[1])
  else:
    wordMix.append(ORIGINALANSWERS[2]) #Otherwise this means that the third word was in 

  if len(usersAnswers[0])< upper < len(userAnswers[0]) + len(userAnswers[1]) and userAnswers[1] not in wordMix: #Same logic applies with the upper bound, but in this case
                                                                                                                #we make sure that this is not already in the wordMix
     wordMix.append(ORIGINALANSWERS[1])
  if upper >= len(userAnswers[0]) + len(userAnswers[1]) and userAnswers[2] not in wordMix:
     wordMix.append(ORIGINALANSWERS[2])   
  
  index = random.randint(3,5)                         #Index of the number chosen
  chosennumber = userAnswers[index]                   #Number chosen that is included in the password
  password.insert(0,chosennumber)
     
  
  usedchars = []
  charlist = ['~', '@', '#', '$', '%', '^', '&'. '*'. '('. '(', '-', '+', '[', ']', '{', '}', '\', '|', '<', '>', '/'. '?']
  if len(password) < passwordLength:
      currlength = len(password)
  while currlength < passwordLength:
      random.shuffle(charlist)
      usedchars.append(charlist[0])                       #List of special characters used
      password[currlength] = charlist[0]                  #password is the final password
       
