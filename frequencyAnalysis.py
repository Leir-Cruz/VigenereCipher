import collections
from checkEspecialCharacter import checkEspecialCharacter
import string
from constants import portuguese, english

class FrequencyAnalysis:
  def calculateFrequency(ciphertextGroup):
    numberOfNormalCharacters = collections.defaultdict(int)
    FrequencyOfNormalCharacters = {}
    ciphertextGroupSize = len(ciphertextGroup)
    totalOfNormalCharacters = 0

    for i in range(ciphertextGroupSize):
      if(not checkEspecialCharacter(ciphertextGroup[i])):
        numberOfNormalCharacters[ciphertextGroup[i] ] += 1
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
  
  def generateCipherGroups(ciphertext, groupSize):
    groups = []
    for i in range(0, len(ciphertext) - groupSize, groupSize):
      group = ciphertext[i:i+groupSize]
      groups.append(group)
    return groups
  
  def calculateShift(firstLetter, secondLetter):
    shift = ord(firstLetter) - ord(secondLetter)
    return shift

  #todo transformar essa função em função que só soma depois de passar pelo normalCharacterIndex
  def generateCipherGroup(ciphertext, spacing):
    cipherGroup = ""
    normalCharacterIndex = 0
    for i in range(len(ciphertext)):
      if(not checkEspecialCharacter(ciphertext[i])):
        if normalCharacterIndex % (spacing) == 0:
          cipherGroup += ciphertext[i]
        normalCharacterIndex += 1  
    return cipherGroup
  
  def findKeyLetter(ciphertext, type="english"):
    if type == "english":
      languageFrequency = english
    else:
      languageFrequency = portuguese
    print(f"grupo: {ciphertext}") #!remove this later 
    frequencyDict = FrequencyAnalysis.calculateFrequency(ciphertext)
    higherFrequencyLetter = max(frequencyDict, key= lambda x: frequencyDict[x])
    print(f"frequência grupo {frequencyDict}") #!remove this later
    higherLanguageFrequencyLetter = max(languageFrequency,  key=lambda x: languageFrequency[x])
    print(f"frequencia alfabeto maior: {higherLanguageFrequencyLetter}") #!remove this later
    print(f"frequencia grupo maior: {higherFrequencyLetter}") #!remove this later
    shift = FrequencyAnalysis.calculateShift(higherFrequencyLetter, higherLanguageFrequencyLetter)
    print(f"shift: {shift}") #!remove this later
    keyLetter = FrequencyAnalysis.caesarCipher('a', shift)
    return keyLetter


  def findKey(ciphertext, keyLength, type="english"):
    key = ""
    for i in range(keyLength): #todo change this
      ciphertextGroup = FrequencyAnalysis.generateCipherGroup(ciphertext[i:len(ciphertext)], keyLength)
      letter = FrequencyAnalysis.findKeyLetter(ciphertextGroup, type) 
      print(f"letra: {letter}") #!remove this later
      key += letter
    return key
