
1.Caesar Cipher Encryption & Decryption Tool

This project is part of my internship (Task 1).  
It is a Python program that can encrypt and decrypt text using the Caesar Cipher algorithm.


2.What is the Caesar Cipher?

The Caesar Cipher is a simple substitution cipher. Each letter in the plaintext shifts by a fixed number of positions in the alphabet.

Example (shift = 3):

- Plaintext: 'HELLO'
- Ciphertext: 'KHOOR'


3.Features

- Encrypts and decrypts text using a user-defined shift value
- Supports uppercase and lowercase letters
- Keeps spaces, digits, and punctuation unchanged
- Menu-based interface:
  - Option to Encrypt
  - Option to Decrypt
  - Option to Exit
- Input validation for:
  - Menu choice
  - Shift value (must be a number between 1 and 25)


4.How the Program Works

  a. The user selects an option:
     - '1' → Encrypt a message  
     - '2' → Decrypt a message  
     - '3' → Exit the program  

  b. The user enters:
     - The message (text)
     - The shift value (e.g., 3, 5, 10)

  c. The program processes each character:
     - If the character is a letter, it shifts it within the alphabet using modular arithmetic.
     - If it is not a letter (like space, punctuation, digit), it is left unchanged.

  d. The transformed message displays as the output.



5.Technologies Used

- Language: Python 3
- Concepts:
  - Functions
  - Loops
  - Conditional statements
  - String manipulation
  - ASCII values (ord() and chr())
  - Modular arithmetic (% 26)

6.File Structure

```text
.
├── caesar_cipher.py   # Main Python script
└── README.md          # Project documentation
```
