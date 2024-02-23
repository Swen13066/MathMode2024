import typing as tp
import string



def encrypt_caesar(plaintext: str, shift: int = 3) -> str:
    """
    Encrypts plaintext using a Caesar cipher.

    >>> encrypt_caesar("PYTHON")
    'SBWKRQ'
    >>> encrypt_caesar("python")
    'sbwkrq'
    >>> encrypt_caesar("Python3.6")
    'Sbwkrq3.6'
    >>> encrypt_caesar("")
    ''
    """
    abc =  string.ascii_lowercase
    ABC = abc.upper()
    abc_new = abc[shift:] + abc[:shift]
    ABC_new = abc_new.upper()
    dict = str.maketrans(abc + ABC, abc_new + ABC_new)

    ciphertext = plaintext.translate(dict)
    # PUT YOUR CODE HERE
    return ciphertext


def decrypt_caesar(ciphertext: str, shift: int = 3) -> str:
    """
    Decrypts a ciphertext using a Caesar cipher.

    >>> decrypt_caesar("SBWKRQ")
    'PYTHON'
    >>> decrypt_caesar("sbwkrq")
    'python'
    >>> decrypt_caesar("Sbwkrq3.6")
    'Python3.6'
    >>> decrypt_caesar("")
    ''
    """
    abc = string.ascii_lowercase
    ABC = abc.upper()
    abc_cip = abc[shift:] + abc[:shift]
    ABC_cip = abc_cip.upper()
    dict = str.maketrans(abc_cip + ABC_cip, abc + ABC)
    plaintext = ciphertext.translate(dict)
    return plaintext


def caesar_breaker_brute_force(ciphertext: str, dictionary: tp.Set[str]) -> int:
    """
    Brute force breaking a Caesar cipher.
    """
    best_shift = 0
    # PUT YOUR CODE HERE
    return best_shift
