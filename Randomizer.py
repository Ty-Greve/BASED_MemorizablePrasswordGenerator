import random



class Randomizer:
  def __init__():
      self.anagramList = __startAnagramList("anagramDictionary.txt")
      pass
   
  def __startAnagramList(filename):
    """This method takes a filename with comma separated anagrams and adds it into a list
       Arguments: String- filename
       Returns: An list of anagrams"""
    #Open file and convert each line into a list
    anagramFile = open(filename, "r")
    anagramList = []
    lineList = anagramFile.readlines()
    #Process file and convert it into a list of anagrams 
    for line in lineList:
      line = line.rstrip('\n')
      line = line.split(',')
      if len(line) > 1:
        anagramList.append(line) 

    return anagramList  
  def findAnagram(word):
    """This method takes a word and finds an appropiate anagram, though
    some words might not have anagrams so in this case then we just return the same word"""
    anagramList = startAnagramList("AnagramDictionary.txt")  
  #----------Find anagram---------------
    #For each tuple in the anagram list 
    for anagrams in anagramList: 
      if word in anagrams: #If our word is in the anagram
        for anagram in anagrams:
          if anagram.lower() != word.lower(): #Find an alternative word (This might need to be bettered)
            return anagram.lower()
    return word    #If no anagram is found then return the same word
  
  def LetterToNumber(letter):
    
    letter.lower()
    
    if letter == 'i':
      return '1';
    elif letter == 'z':
      return '2'
    elif letter == 'e':
      return '3'
    elif letter == 'a':
      return '4'
    elif letter == 's':
      return 5
    elif letter == 'g':
      return 6
    elif letter == 't':
      return 7
    elif letter == 'b':
      return '8'
    elif letter == 'g':
      return '9'
    elif letter == 'o':
      return '0'
