from KasiskiAttack import KasiskiAttack
from frequencyAnalysis import FrequencyAnalysis
from decypher import decypher
from generateKey import generateKeystream

ciphertext = input("digite um texto cifrado: ")
commonNgrams = KasiskiAttack.findCommonNgrams(ciphertext)

keySize = KasiskiAttack.findKeyLength(commonNgrams)
print(f"tamanho da chave: {keySize}")

isPortuguese = int(input("Deseja traduzir o ciphertext usando alfabeto português? Se sim, digite '1', se não, digite '0' "))
if isPortuguese:
  key = FrequencyAnalysis.findKey(ciphertext, keySize, "portuguese")
else:
  key = FrequencyAnalysis.findKey(ciphertext, keySize)

print(f"chave encontrada: {key}")
keystream = generateKeystream(ciphertext, key)
originalText = decypher(ciphertext, keystream)
print(f"mensagem original: {originalText}")