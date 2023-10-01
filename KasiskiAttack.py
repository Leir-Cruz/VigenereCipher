class KasiskiAttack:
  def findCommonNgrams(ciphertext, ngramSize=3):
    ngramsPositions = {}
    ciphertextSize = len(ciphertext)
    for i in range(ciphertextSize):
      ngram = ciphertext[i:i+ ngramSize]
      if ngram not in ngramsPositions.keys():
        ngramsPositions[ngram] = [i]
      else:
        ngramsPositions[ngram].append(i)
    for key in list(ngramsPositions.keys()):
      if len(ngramsPositions[key]) <= 1:
        ngramsPositions.pop(key)
    return ngramsPositions

  def findDistanceBetweenNgrams():
    print("")
  
  def findKeyLength():
    print("")