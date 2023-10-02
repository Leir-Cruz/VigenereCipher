from checkEspecialCharacter import checkEspecialCharacter

def decypher(cyphertext, keystream):
  cyphertextSize = len(cyphertext)
  originalMessage = ""
  normalCharacterIndex = 0
  for i in range(cyphertextSize):
    if checkEspecialCharacter(cyphertext[i]):
      originalMessage += cyphertext[i]
    else:
      decypherCharacter = (ord(cyphertext[i]) - ord(keystream[normalCharacterIndex]) + 26) % 26
      decypherCharacter += ord('a') #* we have to add 'a' to shift our character after module operation
      originalMessage += (chr(decypherCharacter))
      normalCharacterIndex += 1
  return originalMessage