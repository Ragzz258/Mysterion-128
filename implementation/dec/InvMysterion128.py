def InvMysterion128(c, key, NR):
  state=c
  for round in range(NR, 0, -1):
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

    if debug:
      print('----------Round No'+' : '+str(round)+'----------')
      print_s(state,'')


    rc=roundconst(round-1)

    for h in range(4):
      for g in range(4):
        f=state[h][g]
        state[h][g]=f^rc[h][g]
    print_s(state,'After Rev-Constant:')

    #revrse key
    state = np.array( [a^b for a, b in zip(state, key)])
    print_s(state,'After Rev-Key:')
    
    #revrse shift-row
    state = ShiftColumns_128_inv(state)
    print_s(state,'After Rev-ShiftRow:')

    # L-box inverse
    for i in range(4):
      for j in range(4):
        state=rev_lbox(state)
    print_s(state,'After Rev-L-box:')

    # S-box inverse
    for i in range(4):
      for j in range(4):
        tp=sbox_rev(state[i][j])
        state[i][j]=tp
    print_s(state,'after Rev-sbox')


  #intial key removal
  state = np.array( [x ^ y for x, y in zip(state, key)] )
  if (debug or rounds):
    print('After Removing K_0:')
    print()
    for i in range(4):
      for j in range(4):
        t=str(hex(state[i][j]))[2:]
        if len(t)<2:
          t='0'+t
        print(t,' ',end='')
      print() 
  
  print('Message is:')
  temp=''
  for i in range(4):
      for j in range(4):
        t=str(hex(state[i][j]))[2:]
        if len(t)<2:
          t='0'+t
        temp+=t
  temp=temp.upper()
  print(temp)
  return temp
