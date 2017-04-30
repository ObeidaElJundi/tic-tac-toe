
def drawBoard(l):
  print l[0][0],'|',l[0][1],'|',l[0][2]
  print '----------'
  print l[1][0],'|',l[1][1],'|',l[1][2]
  print '----------'
  print l[2][0],'|',l[2][1],'|',l[2][2]

def location(l,x):
  if l<1 or l>9:
    print 'invalid location!\n'
    return False
  row=(l-1)/3
  col=(l%3)-1
  if lst[row][col]==' ':
    global lst
    lst[row][col]='X' if x else 'O'
    return True
  else:
    print 'Location already used!\n'
    return False

def check():
  global lst
  l=lst
  #horizontal check
  for i in range(2):
    if (l[i][0]==l[i][1] and l[i][0]==l[i][2] and l[i][0]!=' '):
      return True
  #vertical check
  for i in range(2):
    if (l[0][i]==l[1][i] and l[0][i]==l[2][i]  and l[0][i]!=' '):
      return True
  #diagonal check
  if (l[0][0]==l[1][1]==l[2][2] or l[0][2]==l[1][1]==l[2][0]) and l[1][1]!=' ':
    return True
  return False


drawBoard([[1,2,3],[4,5,6],[7,8,9]])
xTurn=True
lst=[[' ',' ',' '],[' ',' ',' '],[' ',' ',' ']]
while 1:
  print 'X' if xTurn else 'O', 'turn, where u wanna play?'
  loc=int(raw_input())
  if location(loc,xTurn):
    drawBoard(lst)
    if check():
      print 'X' if xTurn else 'O', 'WON !!!!!!!!!'
      break;
    xTurn = not xTurn
