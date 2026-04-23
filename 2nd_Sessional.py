##def encrypt(text, shift):
##    result = ""
##
##    for char in text:
##        if char.isalpha():
##
##            if char.isupper():
##                result += chr((ord(char) + shift - 65) % 26 + 65)
##            else:
##                result += chr((ord(char) + shift -97) % 26 + 97)
##        else:
##            result +=char
##
##    return result
##
##def decrypt(text, shift):
##    return encrypt(text, -shift)
##
##text = "Hello World"
##shift = 3
##
##encrypted_text = encrypt(text, shift)
##decrypted_text = decrypt(encrypted_text, shift)
##
##
##print("Original text: ", text)
##print("Encrypted text: ", encrypted_text)
##print("Decrypted text: ", decrypted_text)


#playfair cipher implementation

##def generate_key_matrix(key):
##    key = key.upper().replace("J", "I")
##    matrix = []
##    used = set()
##
##    for char in key:
##        if char.isalpha() and char not in used:
##            used.add(char)
##            matrix.append(char)
##
##    for char in "ABCDEFGHIKLMNOPQRSTUVWXYZ":
##        if char not in used:
##            matrix.append(char)
##
##    return [matrix[i: i+5] for i in range(0, 25, 5)]
##
##def find_position(matrix, char):
##    for i in range(5):
##        for j in range(5):
##            if matrix[i][j] == char:
##                return i,j
##
##def preprocess_text(text):
##    text = text.upper().replace("J", "I")
##    text = "".join([ c for c in text if c.isalpha()])
##
##    pairs = []
##    i = 0
##    while i < len(text):
##        a = text[i]
##        b = ''
##        if i+1 < len(text):
##            b= text[i+1]
##
##        if a==b:
##            pairs.append(a + 'X')
##            i += 1
##        else:
##            if b:
##                pairs.append(a+b)
##                i +=2
##            else:
##                pairs.append(a + 'X')
##                i +=1
##    return pairs
##
##def encrypt_playfair(text, key):
##    matrix = generate_key_matrix(key)
##    pairs = preprocess_text(text)
##    result = ""
##
##    for pair in pairs:
##        r1,c1 = find_position(matrix, pair[0])
##        r2,c2 = find_position(matrix, pair[1])
##
##        if r1 == r2:
##            result += matrix[r1][(c1 + 1)%5]
##            result += matrix[r2][(c2+1)%5]
##
##        elif c1==c2:
##            result += matrix[(r1+1)%5][c1]
##            result += matrix[(r2+1)%5][c2]
##        else:
##            result += matrix[r1][c2]
##            result += matrix[r2][c1]
##
##    return result
##
##def decrypt_playfair(text, key):
##    matrix = generate_key_matrix(key)
##    result = ""
##
##    for i in range(0, len(text), 2):
##        r1, c1 = find_position(matrix, text[i])
##        r2, c2 = find_position(matrix, text[i+1])
##
##        if r1==r2:
##            result += matrix[r1][(c1-1)%5]
##            result += matrix[r2][(c2-1)%5]
##
##        elif c1==c2:
##            result += matrix[(r1-1)%5][c1]
##            result += matrix[(r2-1)%5][c2]
##
##        else:
##            result += matrix[r1][c2]
##            result += matrix[r2][c1]
##
##    return result
##
##key = "MONARCHY"
##text = "HELLO"
##
##encrypted = encrypt_playfair(text, key)
##decrypted = decrypt_playfair(encrypted, key)
##
##print("Key Matrix: ")
##for row in generate_key_matrix(key):
##    print(row)
##
##print("\nOriginal Text: ", text)
##print("Encrypted Text: ", encrypted)
##print("Decrypted Text: ", decrypted)



