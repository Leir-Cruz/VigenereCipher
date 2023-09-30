from generateKey import generateKeystream
from checkEspecialCharacter import checkEspecialCharacter

def cypher(message, key):
  messageSize = len(message)
  cyphertext = ""
  try:
    keyStream = generateKeystream(message, key)
  except:
    print("Erro ao gerar KeyStream, tente novamente\n")
  else:
    print(f"Keystream gerado: {keyStream}\n")
    for i in range(messageSize):
      if checkEspecialCharacter(message[i]):
        cyphertext += message[i]
      else:
        cypherCharacter = (ord(message[i]) + ord(keyStream[i])) % 26
        cypherCharacter += ord('a') #* we have to add 'a' to shift our character after module operation
        cyphertext += (chr(cypherCharacter))
  return cyphertext
