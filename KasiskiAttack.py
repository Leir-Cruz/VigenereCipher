from collections import Counter
from checkEspecialCharacter import checkEspecialCharacter

class KasiskiAttack:
  
  def checkValidNgram(ngram):
    return all(checkEspecialCharacter(char) for char in ngram)

  def findDistanceBetweenNgrams(arrayOfPositions):
    arrayOfPositionsSize = len(arrayOfPositions)
    arrayOfDistances = []
    for i in range(arrayOfPositionsSize - 1):
      distance = arrayOfPositions[i + 1] - arrayOfPositions[i]
      arrayOfDistances.append(distance)
    return arrayOfDistances
  
  
  def findCommonNgrams(ciphertext, ngramSize=3):
    ngramsPositions = {}
    ngramsDistances = {}
    ciphertextSize = len(ciphertext)
    normalCharacterIndex = 0
    for i in range(ciphertextSize):
      ngram=""
      for j in range(ciphertextSize - i):
        if len(ngram) >= ngramSize or (checkEspecialCharacter(ciphertext[i]) and ngram==""):
          break
        if not checkEspecialCharacter(ciphertext[j + i]):
          if ngram == "":
            normalCharacterIndex += 1
          ngram += ciphertext[j + i]
      if ngram != "":
        if ngram not in ngramsPositions.keys():
          ngramsPositions[ngram] = [normalCharacterIndex]
        else:
          ngramsPositions[ngram].append(normalCharacterIndex)
    for key in list(ngramsPositions.keys()):
      if len(ngramsPositions[key]) > 1:
        ngramsDistances[key] = KasiskiAttack.findDistanceBetweenNgrams(ngramsPositions[key])
    return ngramsDistances

  def findPotentialDividers(number):
    factors = set()
    for i in range(1, number):
        if number % i == 0:
            factors.add(i)
            factors.add(number//i)
    return sorted(factors)

  def findKeyLength(ngramsDistancesDict):
    dividers = []
    for key in ngramsDistancesDict:
      for i in range(len(ngramsDistancesDict[key])):
        potentialDividers = KasiskiAttack.findPotentialDividers(ngramsDistancesDict[key][i])
        for potentialDivider in potentialDividers:
          dividers.append(potentialDivider)
    countedDividers = Counter(dividers).most_common()
    countedDividersSize = len(countedDividers)
    if(countedDividersSize > 1):
      return countedDividers[1][0]
    elif(countedDividers == 1):
      return countedDividers[0][0]
    else:
      return 0