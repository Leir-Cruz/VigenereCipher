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

  def findKeyLength():
    print("")