from KasiskiAttack import KasiskiAttack
from frequencyAnalysis import FrequencyAnalysis

ciphertext = input("digite um texto cifrado: ")
commonNgrams = KasiskiAttack.findCommonNgrams(ciphertext)

print("Sequências Repetidas e Suas Posições:")
print(commonNgrams)


keySize = KasiskiAttack.findKeyLength(commonNgrams)
print(f"tamanho da chave: {keySize}")


key = FrequencyAnalysis.findKey(ciphertext, keySize)
print(f"resultado final: {key}")