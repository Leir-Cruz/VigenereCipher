from KasiskiAttack import KasiskiAttack

ciphertext = input("digite um texto cifrado: ")
commonNgrams = KasiskiAttack.findCommonNgrams(ciphertext)

print("Sequências Repetidas e Suas Posições:")
print(commonNgrams)


keySize = KasiskiAttack.findKeyLength(commonNgrams)
print(f"Tamanho da chave: {keySize}")
