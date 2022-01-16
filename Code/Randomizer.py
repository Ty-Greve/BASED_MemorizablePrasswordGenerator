import random



class Randomizer:
  def __init__(self):
      self.anagramList =   self.__startList("anagramDictionary.txt")
      self.soundList = self.__startList("outputSound.txt")
   
  def __startList(self, filename):
    """This method takes a filename with comma separated anagrams and adds it into a list
       Arguments: String- filename
       Returns: An list of anagrams"""
    #Open file and convert each line into a list
    myFile = open(filename, "r")
    myList = []
    lineList = myFile.readlines()
    #Process file and convert it into a list of anagrams 
    for line in lineList:
      line = line.rstrip('\n')
      line = line.split(',')
      if len(line) > 1:
        myList.append(line) 

    return myList  
  def __lookup(self, word, itemList):
    """This method takes a word and finds an appropiate anagram, though
    some words might not have anagrams so in this case then we just return the same word"""
    
  #----------Find anagram---------------
    #For each tuple in the anagram list 
    for items in itemList: 
      if word.capitalize() in items: #If our word is in the anagram
        random.shuffle(items)
        return items[0]
    return word    #If no anagram is found then return the same word
  def findAnagram(self, word):
    return self.__lookup(word, self.anagramList)
  def similarSound(self, word):
    return self.__lookup(word,self.soundList)
  def TakeLetterAway(self, word):
    """This method deletes a random amount of letters from random places in the word."""
    length = len(word)
    #number of characters to be deleted
    numofchars = random.randint(0, length)    
    count = 0 

    #Runs as many times as numofchars, and deletes as many characters
    while count < numofchars:
        currlen = len(word)    #current length of the word
        todelete = random.randint(0, currlen)     #index of letter to be deleted
        word = word[:todelete] + word[(todelete+1):]
        count = count + 1

        return word
  
  def __LetterToNumber(self, letter):
    
    letter.lower()
    
    if letter == 'i':
      return '1'
    elif letter == 'z':
      return '2'
    elif letter == 'e':
      return '3'
    elif letter == 'a':
      return '4'
    elif letter == 's':
      return '5'
    elif letter == 'g':
      return '6'
    elif letter == 't':
      return '7'
    elif letter == 'b':
      return '8'
    elif letter == 'g':
      return '9'
    elif letter == 'o':
      return '0'
    else:
      return letter
  def placeNumber(self, word):
    word = list(word)
    print(word)
    for i in range(len(word)):
      word[i] = self.__LetterToNumber(word[i])
    print(str(word))
    word = "".join(word)
    return word
