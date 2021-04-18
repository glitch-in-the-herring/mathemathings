import math

plaintext, key = str(), str()
while not plaintext.isalpha():
	plaintext = input("Plaintext... ").upper()

while not key.isalpha():	
	key = input("Key... ").upper()

if len(key) < len(plaintext):
	key = (key * math.ceil(len(plaintext)/len(key)))[0:(len(key) * math.ceil(len(plaintext)/len(key))) - (len(key) * math.ceil(len(plaintext)/len(key)) % len(plaintext))]
elif len(key) > len(plaintext):
	key = key[0:len(plaintext)]

plaintext_num = [ord(x) - 65 for x in plaintext]
key_num = [ord(x) - 65 for x in key]

ciphertext = ''.join([chr(((plaintext_num[i] + key_num[i]) % 26) + 65) for i in range(len(plaintext))])

print(f"Ciphertext: {ciphertext}")
