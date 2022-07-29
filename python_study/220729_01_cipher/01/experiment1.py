# try to decrypt the file encrypted_text.txt file
#

# Implement a function that we pass the encryption key of a caesar cipher
# and check if the text start to make sense.

def decrypt_caesar_cipher(filepath: str, encryption_key=0) -> None:
    """
    ```
    decrypt_caesar_cipher("encrypted_text.txt")
    ```
    """
    with open(filepath, "r") as f:
        while True:
            line = f.readline()
            if line == "":
                break

            decrypted_line = _decrypt_line(line, encryption_key=encryption_key)
            print(decrypted_line, end="")


def _decrypt_line(line: str, encryption_key=0) -> str:
    NUM_CHARS = 26

    list_line = []
    for c in line:
        c_ascii: int = ord(c)
        if ord("A") <= c_ascii <= ord("Z"):
            # upper case letter
            c_dec = ((c_ascii - ord("A") + encryption_key) % NUM_CHARS) + ord("A")

        elif ord("a") <= c_ascii <= ord("z"):
            # lower case letter
            c_dec = ((c_ascii - ord("a") + encryption_key) % NUM_CHARS) + ord("a")
        else:
            c_dec = c_ascii

        list_line.append(chr(c_dec))

    decrypted_line = "".join(list_line)

    return decrypted_line


def main():
    decrypt_caesar_cipher("encrypted_text.txt", encryption_key=2)


if __name__ == "__main__":
    main()
