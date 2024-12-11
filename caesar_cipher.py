from string import ascii_letters

def encrypt(str,key):
    alphabet = ascii_letters[:26]
    result = ''
    str = str.lower()

    for char in str:
        if char not in alphabet:
            result += char
        else:
            result += alphabet[(alphabet.index(char) + key) % len(alphabet)]
           
    return result


def decrypt(str,key):
  new_key = key * -1
  return encrypt(str,new_key)


 