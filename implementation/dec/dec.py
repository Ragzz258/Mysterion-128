def decrypt(c, k, r):
    c = list(bytearray.fromhex(c))
    k = list(bytearray.fromhex(k))

    # spliting message in blocks 
    c = np.array([c[i*4:(i+1)*4] for i in range(4)])
    k = np.array([k[i*4:(i+1)*4] for i in range(4)])

    cpt = InvMysterion128(c, k, r)
    return cpt
