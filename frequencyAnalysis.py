import collections
from checkEspecialCharacter import checkEspecialCharacter

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
