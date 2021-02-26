import sys
import numpy as np
import os

import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt

def plot_wave(x, path = './wave.png'):
    plt.gcf().clear()
    plt.plot(x)
    plt.xlabel('n')
    plt.ylabel('xn')
    plt.savefig(path)

def plot_ak(a, path = './freq.png'):
    plt.gcf().clear()

    # Only plot the mag of a
    a = np.abs(a)
    plt.plot(a)
    plt.xlabel('k')
    plt.ylabel('ak')
    plt.savefig(path)

def CosineTrans(x, B):
    # TODO
    # implement cosine transform
    B_inv = np.linalg.inv(B)
    a = np.dot(B_inv, x)
    return a

def InvCosineTrans(a, B):
    # TODO
    # implement inverse cosine transform
    x = np.dot(B, a)
    return x

def gen_basis(N):
    # TODO
    B = np.zeros((N,N))

    for n in range(1000):
        for k in range(1000):
            if k == 0:
                B[n][k] = 1/np.sqrt(N)
            else:
                B[n][k] = (np.sqrt(2)/np.sqrt(N))*np.cos((n+0.5)*k*np.pi/N)

    return B

if __name__ == '__main__':
    # Do not modify these 2 lines
    signal_path = sys.argv[1]
    out_directory_path = sys.argv[2]

    # TODO
    orig_data = np.loadtxt(signal_path)
    N = orig_data.shape[0]

    # Generate basis B
    B = gen_basis(N)

    # Calculate a
    a = CosineTrans(orig_data, B)

    # Find frequency's index
    a_abs = np.abs(a)
    f_ind = a_abs.argsort()[-5:][::-1]

    # Calculate f1
    f1_mask = np.zeros(N)
    f1_mask[f_ind[0]] = 1
    f1 = InvCosineTrans(a*f1_mask, B)

    # Calculate f3
    f3_mask = np.zeros(N)
    f3_mask[f_ind[2]] = 1
    f3 = InvCosineTrans(a*f3_mask, B)


    # Do not modify these 3 lines
    plot_ak(a, path=os.path.join(out_directory_path, 'freq.png'))
    plot_wave(f1, path=os.path.join(out_directory_path, 'f1.png'))
    plot_wave(f3, path=os.path.join(out_directory_path, 'f3.png'))

