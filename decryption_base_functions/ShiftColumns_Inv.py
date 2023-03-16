def ShiftColumns_128_inv(state):
    lstate=[]
    for i in range(4):
      for j in range(4):
        lstate.append(state[i][j])
    plstate=[0]*16
    for i in range(16):
      plstate[i]=lstate[p[i]]
    value=[]
    for i in range(4):
      value.append(plstate[4*i:4*i+4])
    return value