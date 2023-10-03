from KasiskiAttack import KasiskiAttack
from frequencyAnalysis import FrequencyAnalysis
from decypher import decypher
from generateKey import generateKeystream

ciphertext = input("digite um texto cifrado: ")
commonNgrams = KasiskiAttack.findCommonNgrams(ciphertext)

keySize = KasiskiAttack.findKeyLength(commonNgrams)
print(f"tamanho da chave: {keySize}")

key = FrequencyAnalysis.findKey(ciphertext, keySize)
print(f"resultado final: {key}")

keystream = generateKeystream(ciphertext, key)
originalText = decypher(ciphertext, keystream)
print(f"mensagem original: {originalText}")