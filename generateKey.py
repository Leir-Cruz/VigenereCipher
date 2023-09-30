def generateKeystream (message, key):
  messageSize = len(message)
  keySize = len(key)
  if messageSize == keySize:
    return key
  elif messageSize > keySize:
    keyStream =  [letter for letter in key]
    for i in range(len(message) - len(key)):
      keyStream.append(keyStream[i % len(key)])
    return "".join(keyStream)
  else:
    return key[0: messageSize]