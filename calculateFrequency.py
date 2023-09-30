import collections
from checkEspecialCharacter import checkEspecialCharacter

def calculateFrequency(ciphertext):
  numberOfNormalCharacters = collections.defaultdict(int)
  FrequencyOfNormalCharacters = {}
  ciphertextSize = len(ciphertext)
  totalOfNormalCharacters = 0

  for i in range(ciphertextSize):
    if(not checkEspecialCharacter(ciphertext[i])):
      numberOfNormalCharacters[ciphertext[i] ] += 1
      totalOfNormalCharacters += 1
  
  for key in numberOfNormalCharacters:
    FrequencyOfNormalCharacters[key] = numberOfNormalCharacters[key] / totalOfNormalCharacters
  
  
  return FrequencyOfNormalCharacters