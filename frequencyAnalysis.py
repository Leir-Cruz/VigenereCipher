import collections
from checkEspecialCharacter import checkEspecialCharacter
from constants import portuguese, english

class FrequencyAnalysis:
  def calculateFrequency(coset):
    numberOfNormalCharacters = collections.defaultdict(int)
    FrequencyOfNormalCharacters = {}
    ciphertextGroupSize = len(coset)
    totalOfNormalCharacters = 0

    for i in range(ciphertextGroupSize):
      if(not checkEspecialCharacter(coset[i])):
        numberOfNormalCharacters[coset[i]] += 1
        totalOfNormalCharacters += 1
    
    for key in numberOfNormalCharacters:
      FrequencyOfNormalCharacters[key] = 100 * (numberOfNormalCharacters[key] / totalOfNormalCharacters)
    
    return FrequencyOfNormalCharacters
  
  def caesarCipher(ciphertext, shift):
    shift = shift % 26
    ciphertextSize = len(ciphertext)
    shiftedCipher = ""
    for i in range(ciphertextSize):
      deslocatedCharacter = (ord(ciphertext[i]) + shift - ord('a')) % 26 + ord('a')
      shiftedCipher += chr(deslocatedCharacter)
    return shiftedCipher
  
  def calculateShift(firstLetter, secondLetter):
    shift = ord(firstLetter) - ord(secondLetter)
    return shift

  def generateCoset(ciphertext, spacing):
    coset = ""
    normalCharacterIndex = 0
    for i in range(len(ciphertext)):
      if(not checkEspecialCharacter(ciphertext[i])):
        if normalCharacterIndex % (spacing) == 0:
          coset += ciphertext[i]
        normalCharacterIndex += 1  
    return coset
  
  def x2CosetValue(cosetFrequency, languageFrequency):
    value = 0
    for key in languageFrequency.keys():
      if key in cosetFrequency.keys():
        value += ((cosetFrequency[key] - languageFrequency[key]) ** 2) / languageFrequency[key]
      else:
        value += languageFrequency[key]
    return value

  def x2CosetFindPossibleLetters(coset, languageFrequency, keyLength):
    shiftDict = {}
    possibleLetters = []
    for i in range(26):
      shiftedCoset = FrequencyAnalysis.caesarCipher(coset, i)
      cosetFrequency = FrequencyAnalysis.calculateFrequency(shiftedCoset)
      cosetX2Value = FrequencyAnalysis.x2CosetValue(cosetFrequency, languageFrequency)
      shiftDict[i] = cosetX2Value
    shiftItems = list(shiftDict.items())
    print(f"coset: {coset}")
    shiftItems.sort(key=lambda item: item[1])
    for j in range(keyLength):
      shift = shiftItems[j][0]
      letter = FrequencyAnalysis.caesarCipher('a', shift)
      possibleLetters.append(letter)
    return possibleLetters


  def findKey(ciphertext, keyLength, languageType="english"):
    key = ""
    if languageType == "english":
      languageFrequency = english
    else:
      languageFrequency = portuguese
    for i in range(keyLength): 
      coset = FrequencyAnalysis.generateCoset(ciphertext[i:len(ciphertext)], keyLength)
      possibleletters = FrequencyAnalysis.x2CosetFindPossibleLetters(coset, languageFrequency, keyLength)
      letter = input(f"Segue as possíveis letras para esse caractere, {possibleletters}, escolha uma: ")
      key += letter
    return key
