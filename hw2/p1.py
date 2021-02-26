import numpy as np
from util import mod_inv


def decode(cipher, key):
    #TODO
    '''
    Decode cipher with public key.

    Arguments:
        cipher: str, cipher text
        key: str, public key

    Return:
        plain: str, plain text
    '''
    letters = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ_.,?!'

    cipher = [letters.index(i) for i in cipher]
    col = int(len(cipher)/3)
    cipher_text = np.reshape(cipher, (-1, 3)).T

    key = [int(k) for k in key.split()]
    key = np.array(key).reshape(3, 3)
    private_key = mod_inv(key)
    
    plain_text = np.mod(private_key @ cipher_text, 31)

    plain2text = []
    for p in plain_text.T.flatten():
        plain2text.append(letters[p])
    #print(''.join(plain2text))
    plain = ''
    plain = ''.join(plain2text)
    return plain