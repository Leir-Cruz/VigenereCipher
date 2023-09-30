from cypher import cypher
from decypher import decypher

if __name__ == "__main__":
  key = input("digite uma chave cifradora: ")
  message = input("digite uma mensagem para ser encriptada: ")

  cyphertext, keystream = cypher(message, key)
  print(f"cyphertext gerado: {cyphertext}")

  originalMessage = decypher(cyphertext, keystream)
  print(f"mensagem original: {originalMessage}")
