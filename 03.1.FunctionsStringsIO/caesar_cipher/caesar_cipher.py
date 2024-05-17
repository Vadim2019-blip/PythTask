def caesar_encrypt(message: str, n: int) -> str:
    """Encrypt message using caesar cipher

    :param message: message to encrypt
    :param n: shift
    :return: encrypted message
    """
    letters = list(message)
    ans = []
    for letter in letters:
        if letter.isupper():
            ans.append(chr(ord('A') + ((ord(letter) - ord('A') + n) % 26)))
        elif letter.islower():
            ans += chr(ord('a') + ((ord(letter) - ord('a') + n) % 26))
        else:
            ans.append(letter)
    return ''.join(ans)
