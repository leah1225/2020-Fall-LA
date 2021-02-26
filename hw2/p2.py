import numpy as np
from util import mod_inv


def get_key(cipher, plain):
    #TODO
    '''
    Calculate public key with cipher text and plain text.

    Arguments:
        cipher: str, cipher text
        plain: str, plain text

    Return:
        key: str, public key
    '''
    letters = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ_.,?!'

    cipher = [letters.index(i) for i in cipher]
    cipher = np.reshape(cipher, (-1, 3)).T

    plain = [letters.index(i) for i in plain]
    plain = np.reshape(plain, (-1, 3)).T

    plain_inv = mod_inv(plain)
    key_array = np.mod(cipher @ plain_inv, 31)

    key = ''

    for k in key_array.reshape(-1):
        key += str(k)
        key += ' '
    key.strip()

    return key

