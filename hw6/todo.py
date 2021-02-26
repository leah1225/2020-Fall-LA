import numpy as np


def svd_compress(imArr, K=50):
    """Compress image array using SVD decomposition.
    Arg:
        imArr: numpy array with shape (height, width, 3).
    Return:
        Compressed imArr: numpy array.
    """
    imArr_compressed = np.zeros(imArr.shape)
    # For each channel
    for ch in range(3):
        # --------------------
        # TODO: 
        #     Compress the image array using SVD decomposition
        # hint:
        #     1. np.linalg.svd
        #     2. np.diag
        #     3. np.dot
        #
        # Your code here
        # ?? = imArr[:,:,ch]
        # imArr_compressed = ??
        u,sigma,v = np.linalg.svd(imArr[:,:, ch])
        u_k = u[:,:K]
        s_k = np.diag(sigma[:K])
        v_k = v[:K,:]
        imArr_compressed[:, :, ch] = np.dot(u_k,np.dot(s_k, v_k))
        # --------------------
        # clip image to 0 ~ 255, DO NOT MODIFY THIS PART
        imArr_compressed[:, :, ch] = np.clip(imArr_compressed[:, :, ch],0,255)
    #imArr_compressed[:, :, 0] = imArr_compressed[:, :, 1]
    return imArr_compressed.astype(np.uint8)