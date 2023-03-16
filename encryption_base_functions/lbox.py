def lbox(state):
    state_8=[[],[],[],[]]
    for i in range(4):
      for j in range(4):
        a=str(hex(state[i][j]))[2:]
        if len(a)<2:
          a='0'+a
        a1=hex_dict[a[0]]
        a2=hex_dict[a[1]]
        state_8[i].append(a1)
        state_8[i].append(a2)
    poly = [0, 0b1000, 0b0011, 0b1111, 0b0101, 0b1111, 0b0011, 0b1000]
    value=[]
    for c in range(4):
      for _ in range(8):
          x = state_8[c][0]
          for i in range(8):
              x ^= MultiplyGF16(state_8[c][i], poly[i])
          state_8[c].pop(0)
          state_8[c].append(x)
    for e in range(4):
      for f in range(4):
        state[e][f]=16*state_8[e][2*f]+state_8[e][2*f+1]
    return state

def MultiplyGF16(a, b, p=0b10011):
    result = 0
    for _ in range(4):
        result ^= (b & 1) * a
        a <<= 1
        a ^= (a >> 4) * p
        b >>= 1
    return result
