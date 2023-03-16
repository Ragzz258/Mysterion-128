#S-box
S=[0,2,10,9,6,4,14,13,1,7,15,8,11,12,3,5]
def Sbox(n):
  a=str(hex(n))[2:]
  if len(a)<2:
          a='0'+a
  a1=hex_dict[a[0]]
  a2=hex_dict[a[1]]
  r=S[a1]*16+S[a2]
  return r
