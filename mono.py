plainset=['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z',' ']
cipherset=['f','e','d','q','r','s','z','y','x','a','c','b','p','u','v','h','w','g','n','i','o','t','k','m','j','l',' ']


plaintext="meet me at the coffee shop tomorrow"
ciphertext=""

print('=============================================MONOALPHABETIC CIPHER ENCRYPTION====================================')
for x in range(0,len(plaintext)):
    for y in range(0,len(plainset)):
        if (plaintext[x]==plainset[y]):
            ciphertext+=cipherset[y]
            
print(plaintext)
print(ciphertext)

plaintext=""
ciphertext="prri pr fi iyr dvssrr nyvh ivpvggvk"

print('=============================================MONOALPHABETIC CIPHER DECRYPTION====================================')
for x in range(0,len(ciphertext)):
    for y in range(0,len(cipherset)):
        if (ciphertext[x]==cipherset[y]):
            plaintext+=plainset[y]
print(ciphertext)           
print(plaintext)
