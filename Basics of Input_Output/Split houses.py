integer = int(input())
string = input()

strlst = list(string)

if integer > 1:
  if strlst[0] == 'H' and strlst[1] == '.':
    strlst[1] = 'B'

  if strlst[-1] == 'H' and strlst[-2] == '.':
    strlst[-2] = 'B'

  for i in range(0, integer):
    if strlst[i] == '.':
      strlst[i] = 'B'

  for i in range(1, integer-1):
    if (strlst[i] == 'H') & (strlst[i+1] == '.'):
      strlst[i+1] = 'B'

  strin = ''.join(strlst)

  is_possible = True
  for i in range(integer-1):
    if strin[i] =='H' and strin[i+1]=='H':
      is_possible = False
      break
    
  if is_possible == False:
    print('NO')
  else:
    print('YES')
    print(strin)

else:
  
  if string == '.':
    string = 'B'
    print('YES')
    print(string)

  elif string == 'H':
    print('YES')
    print(string)
    
  else:
    print('NO')
