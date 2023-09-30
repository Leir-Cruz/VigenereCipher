from generateKey import generateKeystream

if __name__ == "__main__":
  key = input("digite uma chave cifradora: ")
  cyphertext = input("digite uma mensagem para ser encriptada: ")

  keystream = generateKeystream(cyphertext, key)
  print(f"KeyStream gerado: {keystream}")

  