from collections import Counter

class KasiskiAttack:
  
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
    for i in range(ciphertextSize):
      ngram = ciphertext[i:i+ ngramSize]
      if ngram not in ngramsPositions.keys():
        ngramsPositions[ngram] = [i]
      else:
        ngramsPositions[ngram].append(i)
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
    countedDividers = Counter(dividers)
    return countedDividers.most_common(1)[0][0] #todo do not counter number one!!!