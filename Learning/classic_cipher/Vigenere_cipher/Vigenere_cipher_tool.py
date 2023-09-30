


def decrypt(encryptext, key):
    plaintext = ""
    for i in range(0, len(encryptext)):
        if encryptext[i].isalpha():
            if encryptext[i].isupper():
                plaintext += chr(( ((ord(encryptext[i]) - ord('A')) - (ord(key[i % len(key)].upper()) - ord('A'))) % 26) + ord('A'))
            else :
                plaintext += chr(( ((ord(encryptext[i]) - ord('a')) - (ord(key[i % len(key)].lower()) - ord('a'))) % 26) + ord('a'))
        else:
            print(encryptext[i])
    return plaintext


def encrypt(plaintext, key):
    encryptext = ""
    for i in range(0, len(plaintext)):
        if plaintext[i].isalpha():
            if plaintext[i].isupper():
                encryptext += chr(((ord(plaintext[i]) - ord('A') + ord(key[i % len(key)].upper()) - ord('A')) % 26) + ord('A'))
            else :
                encryptext += chr(((ord(plaintext[i]) - ord('a') + ord(key[i % len(key)].lower()) - ord('a')) % 26) + ord('a'))
        else:
            print(plaintext[i])
    return encryptext


def main():
    plaintext = str(input('input string\n>>'))
    select = int(input("input 1 or 2 (Encode / Decode)\n>>"))
    key = str(input("input key\n>>"))
    if select == 1 :
        print("encryptext :", encrypt(plaintext, key))
    else :
        print("decryptext :", decrypt(plaintext, key))


if __name__ == "__main__":
    main()

