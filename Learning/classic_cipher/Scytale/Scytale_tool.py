
def en_or_decrypt(plaintext, rows, letters):
    encryptext = ""
    arr = [[-1 for _ in range(letters)] for _ in range(rows)]
    x = 0
    y = 0
    for i in plaintext :
        arr[x][y] = i
        y+=1
        if y == letters :
            y = 0
            x += 1
    for i in range(0, letters):
        for j in range(0, rows):
            if arr[j][i] == -1:
                encryptext += " "
            else :
                encryptext += str(arr[j][i])
    return encryptext


def main():
    plaintext = str(input('input string\n>>'))
    select = int(input("input 1 or 2 (Encode / Decode)\n>>"))
    letters = int(input("How many letters of row\n>>"))
    rows = len(plaintext) // letters
    if len(plaintext) % letters > 0:
        rows += 1
    if select == 1 :
        print(f"encryptext:{en_or_decrypt(plaintext, rows, letters)}|END")
    else :
        rows, letters = letters, rows
        print(f"decryptext:{en_or_decrypt(plaintext, rows, letters)}|END")


if __name__ == "__main__":
    main()