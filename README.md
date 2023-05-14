# Simple Text Encrypter

This is a simple text encrypter application built using the Tkinter library in Python. It provides two encryption methods: Ceasar Cipher and Vigenere Cipher.

## Features

- Open and save text files
- Encrypt and decrypt text using Ceasar Cipher or Vigenere Cipher
- Specify encryption parameters such as key (for Ceasar Cipher) or keyword/phrase (for Vigenere Cipher)

## Requirements

- Python 3.x
- Tkinter library

## Installation

1. Clone the repository or download the project files.
2. Install the required dependencies using the following command:
   ```
   pip install tkinter
   ```

## Usage

1. Run the application by executing the following command:
   ```
   python encrypter.py
   ```

2. The application window will appear.
3. Use the "Open" button to select a text file to open and display its content in the text editor.
4. Use the "Save As..." button to save the current text in the text editor to a text file.
5. Select the desired encryption method (Ceasar Cipher or Vigenere Cipher) by choosing the corresponding radio button.
6. If using Ceasar Cipher, enter the encryption key in the "Key" field.
7. If using Vigenere Cipher, enter the encryption keyword/phrase in the "Keyword" field.
8. Click the "Encrypt" button to encrypt the text in the editor using the selected encryption method and parameters.
9. Click the "Decrypt" button to decrypt the encrypted text in the editor using the selected encryption method and parameters.
10. The encrypted or decrypted text will be displayed in the text editor.

## Additional Information

- The Ceasar Cipher shifts each letter in the message by a certain number of positions in the alphabet based on the encryption key.
- The Vigenere Cipher is a polyalphabetic cipher that uses a keyword or phrase to encrypt the message. It shifts each letter by a different "key" value based on the corresponding letter in the keyword/phrase.
- The application provides information about its usage and the encryption methods in the information panel within the main window.

Feel free to explore and modify the code according to your requirements.
