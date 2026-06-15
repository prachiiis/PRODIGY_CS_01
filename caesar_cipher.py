# Caesar Cipher Encryption Function
def encrypt(text, shift):
    result = ""

    for char in text:

        # Encrypt uppercase letters
        if char.isupper():
            result += chr((ord(char) - ord('A') + shift) % 26 + ord('A'))

        # Encrypt lowercase letters
        elif char.islower():
            result += chr((ord(char) - ord('a') + shift) % 26 + ord('a'))

        # Keep spaces, numbers and symbols unchanged
        else:
            result += char

    return result


# Caesar Cipher Decryption Function
def decrypt(text, shift):
    result = ""

    for char in text:

        # Decrypt uppercase letters
        if char.isupper():
            result += chr((ord(char) - ord('A') - shift) % 26 + ord('A'))

        # Decrypt lowercase letters
        elif char.islower():
            result += chr((ord(char) - ord('a') - shift) % 26 + ord('a'))

        # Keep spaces, numbers and symbols unchanged
        else:
            result += char

    return result


# Main Program
print("===== Caesar Cipher Program =====")

message = input("Enter your message: ")
shift = int(input("Enter shift value: "))

print("\nChoose Operation")
print("1. Encrypt")
print("2. Decrypt")

choice = input("Enter choice (1/2): ")

if choice == "1":
    encrypted = encrypt(message, shift)
    print("\nEncrypted Message:", encrypted)

elif choice == "2":
    decrypted = decrypt(message, shift)
    print("\nDecrypted Message:", decrypted)

else:
    print("Invalid Choice!")
