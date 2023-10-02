from generateKey import generateKeystream
from checkEspecialCharacter import checkEspecialCharacter

def cypher(message, key):
  messageSize = len(message)
  cyphertext = ""
  try:
    keystream = generateKeystream(message, key)
  except:
    print("Erro ao gerar KeyStream, tente novamente")
  else:
    print(f"Keystream gerado: {keystream}")
    for i in range(messageSize):
      if checkEspecialCharacter(message[i]):
        cyphertext += message[i]
      else:
        cypherCharacter = (ord(message[i]) + ord(keystream[i]) - 2 * ord('a')) % 26
        cypherCharacter += ord('a')  # shift
        cyphertext += chr(cypherCharacter)
  return cyphertext, keystream
