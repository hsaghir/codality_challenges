import math
def binaryGap(N):
'''
this function finds the max gap length in the
binary vertion of the input

input N -> a positive integer
output -> returns the max binary gap length

example : "100101"->2 
'''

  numOnes=0;counter=0;gapL=0;
  while N>0:
    newN=math.floor(N/2)
    modulus=N-newN*2
    N=newN
    if modulus:
      numOnes+=1
    if numOnes:
      if numOnes%2:
        counter+=1
      else:
        if counter-1>gapL:
          gapL=counter-1
        counter=1
        numOnes=1
  return gapL

c=binaryGap(529)
print c