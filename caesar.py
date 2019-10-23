def encrypt_caesar(plaintext: str) -> str:
    """
    >>> encrypt_caesar("PYTHON")
    'SBWKRQ'
    >>> encrypt_caesar("python")
    'sbwkrq'
    >>> encrypt_caesar("Python3.6")
    'Sbwkrq3.6'
    >>> encrypt_caesar("")
    ''
    """
    ciphertext = ''
    for character in plaintext:
        if character.isalpha():
            shift = ord(character) + 3
            if ord('Z') < shift < ord('a') or shift > ord('z'):
                shift -= 26
            ciphertext += chr(shift)
        else:
            ciphertext += character
    return ciphertext


def decrypt_caesar(ciphertext: str) -> str:
    """
    >>> decrypt_caesar("SBWKRQ")
    'PYTHON'
    >>> decrypt_caesar("sbwkrq")
    'python'
    >>> decrypt_caesar("Sbwkrq3.6")
    'Python3.6'
    >>> decrypt_caesar("")
    ''
    """
    plaintext = ''
    for character in ciphertext:
        if character.isalpha():
            shift = ord(character) - 3
            if ord('a') > shift > ord('Z') or shift < ord('A'):
                shift += 26
            plaintext += chr(shift)
        else:
            plaintext += character
    return plaintext
