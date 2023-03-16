def Mysterion128(key, m, NR):
  temp=''
  # adding key initially
  print_s(m,'Initially Message is:')
  print() 

  state = np.array( [x ^ y for x, y in zip(key, m)] )
  #print(state)
  if (debug or rounds):
    print('After Adding K_0:')
    print()
    for i in range(4):
      for j in range(4):
        t=str(hex(state[i][j]))[2:]
        if len(t)<2:
          t='0'+t
        print(t,' ',end='')
      print() 

  for round in range(1, NR + 1):
    if debug:
      print('------------Round No'+' : '+str(round)+'------------------')
      print()
    # S-box
    for i in range(4):
      for j in range(4):
        tp=Sbox(state[i][j])
        state[i][j]=tp
    print_s(state,'After S-box Operation:')

    # L-box
    for i in range(4):
      for j in range(4):
        state=lbox(state)
    print_s(state,'After L-box Operation:')

    # ShiftColumns 128-bit
    state = ShiftColumns_128(state)
    print_s(state,'After Shift Column:')

    #key addition
    state = np.array( [x ^ y for x, y in zip(key, state)])
    print_s(state,'After Key Addition:')

    #round Constant
    rc=roundconst(round-1)
    state = np.array( [x ^ c for x, c in zip(state, rc)])
    print_s(state,'After Round Constant:')

    if rounds==True:
      print()
      print('Round No : '+str(round))
      for i in range(4):
        for j in range(4):
          t=str(hex(state[i][j]))[2:]
          if len(t)<2:
            t='0'+t
          print(t,' ',end='')
        print()
      print()
  
  print('Ciphertext is: ')
  for i in range(4):
      for j in range(4):
        t=str(hex(state[i][j]))[2:]
        if len(t)<2:
          t='0'+t
        temp+=t
  temp=temp.upper()
  print(temp)
  return temp
