def createPassword(userAnswers, passwordLength):

  for object in userAnswers:
    object.strip()                                                      #Removes leading and trailing whitespaces
    object.replace(" ", "")                                             #Removes whitespace from within

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
#Check the upper and lower boundaries with the mega string
  if lower <  len(userAnswers[0]):
    wordMix.append(userAnswers[0])
  elif len(usersAnswers[0])< lower < len(userAnswers[0] + len(userAnswers[1]):
    wordMix.append(userAnswers[1])
  else:
    wordMix.append(userAnswers[2])

  if len(usersAnswers[0])< upper < len(userAnswers[0] + len(userAnswers[1]) and userAnswers[1] not in wordMix:
      wordMix.append(userAnswers[1])
  if upper >= len(userAnswers[0] + len(userAnswers[1]) and userAnswers[2] not in wordMix:
     wordMix.append(userAnswers[2])   
  
  chosennumber = random.randint(3,5)                         #Index of the number chosen
  password.insert(0,chosennumber)
  
  charlist = ['~', '@', '#', '$', '%', '^', '&'. '*'. '('. '(', '-', '+', '[', ']', '{', '}', '\', '|', '<', '>', '/'. '?']
  if len(password) < passwordLength:
      currlength = len(password)
  while currlength < passwordLength:
      random.shuffle(charlist)
      password[currlength] = charlist[0]
       
