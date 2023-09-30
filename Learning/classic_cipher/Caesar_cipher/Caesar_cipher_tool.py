def Caesar(plaintext, shift): 
    encryptext = ""
    for i in plaintext:
        if i.isalpha():
            if i.isupper():
                encryptext_char = chr(( ord(i) - ord('A') +shift ) % 26 + ord('A'))
            else:
                encryptext_char = chr(( ord(i) - ord('a') +shift ) % 26 + ord('a'))
        else :
            encryptext_char = chr(ord(i) + shift)
        encryptext += encryptext_char
    return encryptext

def main():
    plaintext = str(input('input string\n>>'))
    select = int(input("input 1 or 2 (right shift / left shift)\n>>"))
    shift = int(input("input shift\n>>"))
    if select == 1 :
        print("encryptext :", Caesar(plaintext, shift))
    else :
        print("encryptext :", Caesar(plaintext, shift*(-1)))

if __name__ == "__main__":
    main()




