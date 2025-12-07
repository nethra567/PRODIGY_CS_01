def caesar_cipher(text, shift, mode):
    result = ""

    for char in text:
        if char.isupper():
            start = ord('A')
            result += chr((ord(char) - start + (shift if mode == "encrypt" else -shift)) % 26 + start)

        elif char.islower():
            start = ord('a')
            result += chr((ord(char) - start + (shift if mode == "encrypt" else -shift)) % 26 + start)

        else:
            result += char

    return result


print("Caesar Cipher Encryption/Decryption Tool")

while True:
    print("\nSelect an option:")
    print("1. Encrypt a message")
    print("2. Decrypt a message")
    print("3. Exit")

    choice = input("Enter your choice (1/2/3): ")

    if choice == '1':
        mode = "encrypt"
    elif choice == '2':
        mode = "decrypt"
    elif choice == '3':
        print("Exiting the program")
        break
    else:
        print("Invalid choice! Please select 1, 2, or 3.")
        continue

    message = input("\nEnter your message: ")

    try:
        shift = int(input("Enter shift value (1–25): "))
        if shift < 1 or shift > 25:
            print("Shift value must be between 1 and 25!")
            continue
    except ValueError:
        print("Please enter a valid number for shift!")
        continue

    result = caesar_cipher(message, shift, mode)
    print(f"\nResult after {mode}: {result}")
