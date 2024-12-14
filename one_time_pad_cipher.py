"""
    one time pad

"""
import random
class Onetime:
    
    def encrypt(self, str):
        key = []
        cipher = []
        plain = [ord(i) for i in str]

        for i in plain:
            k = random.randint(1,100)
            c = (i + k) * k
            cipher.append(c)
            key.append(k)
        return cipher, key

    def decrypt(self, cipher, key):
        plain = []
        for i in range(len(key)):
            p = int((cipher[i] - key[i] ** 2) / key[i])
            plain.append(chr(p))
        result = "".join([i for i in plain])
        return result
