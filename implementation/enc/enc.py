def encrypt(m, k, r):

    m = list(bytearray.fromhex(m))
    k = list(bytearray.fromhex(k))

    m = np.array([m[i*4:(i+1)*4] for i in range(4)])
    k = np.array([k[i*4:(i+1)*4] for i in range(4)])

    ct = Mysterion128(k, m, r)
    
    return ct
