import random
import string

encryption = random.randint(1, 5)

chars = " " + string.punctuation + string.digits + string.ascii_letters
chars = list(chars)

normal_text = input("Enter you password: ")
cipher_text = ""
new_cipher = ""

if encryption == 1:
    key = ['>', '*', 'K', 'Y', 'W', '?', '1', '%', '$', ' ', '8', 's', 'k', '=', '`', 'M', ';', '\\', '2', '/', '4',
           'b', 'B', '~', '&', 'c', '3', ':', '<', 'h', 'L', 'v', 'j', 'l', '.', '|', '"', 'n', 'P', 'F', '_', 'C', 'G',
           '^', 'Q', '(', 'z', '6', 'o', 'r', 'q', 'D', 'g', 'X', 'y', ']', 'i', '}', 'u', 'p', 't', '{', '[', '!', '0',
           'x', 'A', 'J', 'T', '+', 'w', 'a', "'", '#', '@', 'Z', 'm', 'N', 'V', '7', 'R', ')', 'O', 'd', '9', 'S', 'E',
           'f', '-', ',', 'H', 'e', 'U', 'I', '5']
    for letter in normal_text:

        index = chars.index(letter)
        cipher_text += key[index]

    new_cipher += "X3b$uE5vP9sA1rZ2wC4mH6nT8gF7jL0qKtOyDz" + cipher_text + "81^1mnfa.,1&adFra1*13T1maul/1dADmb"


if encryption == 2:
    key = ['(', ')', '\\', 'm', '.', 'h', '0', ']', 'o', 'k', 'O', 'B', '8', ' ', 'J', 'x', 'Z', 'U', 'u', '@', 'K',
           'E', ',', '}', '*', 'v', 'l', 'y', 'S', '`', 's', '<', '5', 'e', '+', 'z', '4', 'n', 'i', '1', ':', 'V', 'T',
           'C', 'W', '$', 'c', ';', '{', 'g', 'd', 'G', '3', 'D', 't', 'w', 'H', '%', '"', 'a', 'p', '[', 'r', 'Y', 'M',
           'q', '&', 'Q', 'N', 'f', 'b', '6', 'A', '#', "'", '|', '9', '?', '>', '^', '7', '2', '_', 'F', '!', '~', '-',
           'X', 'I', '/', 'R', 'P', '=', 'L', 'j']

    for letter in normal_text:
        index = chars.index(letter)
        cipher_text += key[index]

    new_cipher += "J6dC9eI3uK0oM4kT8zYxP2sB7vA1rZ5wSfGnH" + cipher_text + "72&9jeKx0$4LbVp8u5Rc1umM;kf35UF(A%Q"


if encryption == 3:
    key = ['l', 'U', '7', 'd', 'E', 'e', '3', 'm', 'B', '6', '\\', '}', '.', "'", '~', ';', '0', ' ', '^', '&', 'L', '*', 'D', 'x', ')', 'C', '9', 'P', ']', '|', '#', '/', ',', '{', 'X', '5', 'b', 'f', '"', '(', '8', '`', '-', 'n', '!', '[', 'Q', 'R', '=', 'z', 'p', 'o', 'W', ':', '4', 'w', 'k', '2', 'T', 'I', '@', 'G', 'h', 'u', '?', 'S', 't', 'Z', 'v', 's', 'r', 'q', '+', 'N', 'y', '1', 'O', 'i', '<', 'g', 'K', 'A', '$', '>', '_', 'V', 'j', 'H', '%', 'c', 'Y', 'F', 'J', 'M', 'a']

    for letter in normal_text:
        index = chars.index(letter)
        cipher_text += key[index]

    new_cipher += "G2yT5vBxP1b$uC4wN6mH9nL3zW7kQ0aD8eSfR" + cipher_text + "P5s@kRjFzLw6qXe2nDcnGh24&)g!2tYY"


if encryption == 4:
    key = ['O', '@', '_', '^', '(', 'A', 'I', 'Z', 'B', '|', '}', ',', 'c', '6', "'", 'K', 'o', 'u', ')', '<', 'H', 'y', 'E', 'f', 'm', '#', 'b', 'v', 'V', 'w', '%', 'Q', '`', 'C', 'l', '2', 'N', '+', '{', 'h', '1', ']', ':', 'k', 'i', 'x', '*', 'p', '"', '4', 'z', 'e', '.', 'D', '$', ' ', '!', '9', 'X', 'd', '8', 'J', 'L', 'F', 's', 'j', '7', '0', '~', '-', 'g', '3', '&', 'n', 'Y', 'W', '/', '=', '5', ';', 't', 'S', '>', '[', 'R', 'a', 'T', '?', 'P', 'G', 'U', 'q', 'r', 'M', '\\']

    for letter in normal_text:
        index = chars.index(letter)
        cipher_text += key[index]

    new_cipher += "E5vBpQlA9rZ2wS6xD7cF1gH3jM0kT4zN8uYiO" + cipher_text + "G9Ynaf&6)=ev#mAiEhW3xUo7tBpQl';r"


if encryption == 5:
    key = ['G', 'T', ')', 'n', 'J', '>', '4', 'x', '(', 'w', 'a', '\\', 'h', 'e', '=', 'f', 'r', 'u', '2', 'I', 'E', '{', 'H', ' ', '%', '6', 'g', 'v', '1', 'F', 'R', 'A', '7', 'W', '5', "'", 'c', '"', ':', '|', 'i', 'P', 'V', '0', 'C', '!', 'U', '#', '$', 'S', 'b', '}', 'y', 'D', 'Z', 'q', 'd', 'l', 'M', 'B', ';', ']', 's', 't', 'p', '.', 'O', '-', '^', '[', '/', 'z', '*', 'K', '@', 'k', 'j', 'X', '~', '_', 'Y', '+', 'o', '<', '8', 'm', '`', '9', ',', 'L', '3', '&', 'N', 'Q', '?']


    for letter in normal_text:
        index = chars.index(letter)
        cipher_text += key[index]

    new_cipher += "R7kTzYxP4sCmW9nHdQ2fGvBjL6aV1eU8oI3uK" + cipher_text + "T2z$uHd\\']19lmMnaNfA8rVbC1gMwX"


print(f"Password: {normal_text}")
print(f"Encryption: {new_cipher}")


