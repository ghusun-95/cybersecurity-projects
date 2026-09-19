import string

def caesar_encrypt(message, key):
    shift = key % 26
    cipher = str.maketrans(string.ascii_lowercase, string.ascii_lowercase[shift:] + string.ascii_lowercase[:shift])
    encrypted_message = message.lower().translate(cipher)
    return encrypted_message

def caesar_decrypt(encrypted_message, key):
    shift = 26 - (key % 26)
    cipher = str.maketrans(string.ascii_lowercase, string.ascii_lowercase[shift:] + string.ascii_lowercase[:shift])
    message = encrypted_message.translate(cipher)
    return message

# استخدام نصوص بالإنجليزية لتفادي خطأ الترميز
message = input("Enter the message to encrypt: ")
key = int(input("Enter the shift key number: "))

# التشفير والطباعة
encrypted_message = caesar_encrypt(message, key)
print(f'Encrypted message: {encrypted_message}')

# فك التشفير والطباعة
decrypted_message = caesar_decrypt(encrypted_message, key)
print(f'Decrypted message: {decrypted_message}')