def sbox_rev(n):
    a=str(hex(n))[2:]
    if len(a)<2:
            a='0'+a
    a1=hex_dict[a[0]]
    a2=hex_dict[a[1]]
    
    r=S.index(a1)*16+S.index(a2)
    return r