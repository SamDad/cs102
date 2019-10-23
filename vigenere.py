def encrypt_vigenere(plaintext, keyword):
    """
    Encrypts plaintext using a Vigenere cipher.
    >>> encrypt_vigenere("PYTHON", "A")
    'PYTHON'
    >>> encrypt_vigenere("python", "a")
    'python'
    >>> encrypt_vigenere("ATTACKATDAWN", "LEMON")
    'LXFOPVEFRNHR'
    """
    ciphertext = ''
    key = ''
    while len(key) < len(plaintext):
        key += keyword
    for index in range(len(plaintext)):
        if plaintext[index].isalpha():
            shift = ord(key[index])
            shift -= ord('a') if 'a' <= plaintext[index] <= 'z' else ord('A')
            code = ord(plaintext[index]) + shift
            if 'a' <= plaintext[index] <= 'z' and code > ord('z'):
                code -= 26
            elif 'A' <= plaintext[index] <= 'Z' and code > ord('Z'):
                code -= 26
            ciphertext += chr(code)
        else:
            ciphertext += plaintext[index]
    return ciphertext


def decrypt_vigenere(ciphertext, keyword):
    """
    Decrypts a ciphertext using a Vigenere cipher.
    >>> decrypt_vigenere("PYTHON", "A")
    'PYTHON'
    >>> decrypt_vigenere("python", "a")
    'python'
    >>> decrypt_vigenere("LXFOPVEFRNHR", "LEMON")
    'ATTACKATDAWN'
    """
    plaintext = ''
    key = ''
    while len(key) < len(ciphertext):
        key += keyword
    for index in range(len(ciphertext)):
        if ciphertext[index].isalpha():
            shift = ord(key[index])
            shift -= ord('a') if 'a' <= ciphertext[index] <= 'z' else ord('A')
            code = ord(ciphertext[index]) - shift
            if 'a' <= ciphertext[index] <= 'z' and code < ord('a'):
                code += 26
            elif 'A' <= ciphertext[index] <= 'Z' and code < ord('A'):
                code += 26
            plaintext += chr(code)
        else:
            plaintext += ciphertext[index]
    return plaintext
