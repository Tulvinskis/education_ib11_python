def encrypt_caesar(msg, shift=3):
    result = ""
    for char in msg:
        if char.isalpha():
            ascii_offset = ord('а') if char.islower() else ord('А')
            encrypted_char = chr((ord(char) - ascii_offset + shift) % 32 + ascii_offset)
            result += encrypted_char
        else:
            result += char
    return result

def decrypt_caesar(msg, shift=3):
    return encrypt_caesar(msg, -shift)

msg = "Да здравствует салат Цезарь!"
shift = 3
encrypted = encrypt_caesar(msg, shift)
decrypted = decrypt_caesar(encrypted, shift)
print(encrypted)
print(decrypted)