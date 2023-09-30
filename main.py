from cypher import cypher

if __name__ == "__main__":
  key = input("digite uma chave cifradora: ")
  message = input("digite uma mensagem para ser encriptada: ")

  cyphertext = cypher(message, key)
  print(f"cyphertex gerado: {cyphertext}")
