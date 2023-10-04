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
    if shift < 0:
      shift += 25
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

  def x2CosetFindLetter(coset, languageFrequency):
    shiftDict = {}
    for i in range(26):
      shiftedCoset = FrequencyAnalysis.caesarCipher(coset, i)
      cosetFrequency = FrequencyAnalysis.calculateFrequency(shiftedCoset)
      cosetX2Value = FrequencyAnalysis.x2CosetValue(cosetFrequency, languageFrequency)
      shiftDict[i] = cosetX2Value
    shift = min(shiftDict, key=shiftDict.get)
    letter = FrequencyAnalysis.caesarCipher('a', shift)
    return letter


  def findKey(ciphertext, keyLength, languageType="english"):
    key = ""
    if languageType == "english":
      languageFrequency = english
    else:
      languageFrequency = portuguese
    for i in range(keyLength): 
      coset = FrequencyAnalysis.generateCoset(ciphertext[i:len(ciphertext)], keyLength)
      letter = FrequencyAnalysis.x2CosetFindLetter(coset, languageFrequency) 
      key += letter
    return key
