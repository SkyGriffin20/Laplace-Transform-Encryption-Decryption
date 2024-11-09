# Custom String Encryption and Decryption

## Overview
This project implements a custom encryption and decryption algorithm for strings using mathematical transformations based on a provided integer `r`. It generates encrypted text along with keys (quotients) for decryption, which are used to reverse the encryption process and retrieve the original message.

## Table of Contents
- [Features](#features)
- [Technologies Used](#technologies-used)
- [Installation](#installation)
- [Usage](#usage)
- [Future Improvements](#future-improvements)
- [Contact](#contact)

## Features
- **Encryption**: Transforms each character in the input string into an encrypted character using a mathematical formula with a given base `r` value.
- **Decryption**: Recovers the original string using both the encrypted string and the quotients (keys) generated during encryption.

## Technologies Used
- **Python**: Core programming language.

## Installation
1. Clone or download this repository.
2. Ensure you have Python installed on your system.

## Usage
1. **Encryption**:
   - Use the `encrypt_string(input_string, r)` function, where:
     - `input_string` is the string to be encrypted.
     - `r` is the base integer used for transformation.
   - Example:
     ```python
     encrypt_string('ROUHIN', 2)
     ```
     ```
     Input:  SKYGRIFFIN
     Keys: [0, 5, 76, 120, 1595, 3899, 12288, 56713, 385654, 2681934]
     Encrypted Text:  SBXPBB`VDT
     ```
     
2. **Decryption**:
   - Use the `decrypt_string(encrypted_string, k_values, r)` function, where:
     - `encrypted_string` is the string obtained from encryption.
     - `k_values` is the list of quotient keys from encryption.
     - `r` is the base integer used for transformation.
   - Example:
     ```python
     decrypt_string('RXPVNF', [0, 6, 64, 137, 797, 6065], 2)
     ```
     ```
     Decrypted Text:
     SKYGRIFFIN
     ```
     
## Future Improvements
- Add support for case sensitivity in encryption and decryption.
- Expand to include special characters and numbers.
- Implement error handling for unsupported inputs.

## Contact
skygriffin20.contact@gmail.com
