from checkEspecialCharacter import checkEspecialCharacter

def decypher(cyphertext, keystream):
  cyphertextSize = len(cyphertext)
  originalMessage = ""

  for i in range(cyphertextSize):
    if checkEspecialCharacter(cyphertext[i]):
      originalMessage += cyphertext[i]
    else:
      decypherCharacter = (ord(cyphertext[i]) - ord(keystream[i]) + 26) % 26
      decypherCharacter += ord('a') #* we have to add 'a' to shift our character after module operation
      originalMessage += (chr(decypherCharacter))
  return originalMessage