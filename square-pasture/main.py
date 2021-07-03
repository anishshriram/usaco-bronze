f = open('square.in')
f = f.readlines()

firstRect = []
secondRect = []

for i in range(len(f)):
  if i % 2 == 0:
    firstRect.append(f[i].strip('\n').split(' '))
  else:
    secondRect.append(f[i].strip('\n').split(' '))

answer = ''

x1A = firstRect[0][0]
x2A = firstRect[0][2]
y1A = firstRect[0][1]
y2A = firstRect[0][3]

x1B = secondRect[0][0]
x2B = secondRect[0][2]
y1B = secondRect[0][1]
y2B = secondRect[0][3]

x = [x1A, x2A, x1B, x2B]
y = [y1A, y2A, y1B, y2B]

xInt = [int(i) for i in x]
yInt = [int(i) for i in y]

xSort = sorted(xInt)
ySort = sorted(yInt)

xDiff = xSort[3] - xSort[0]
yDiff = ySort[3] - ySort[0]

if (xDiff > yDiff):
  answer = str(xDiff * xDiff)
elif (yDiff > xDiff):
  answer = str(yDiff * yDiff)
else:
  answer = str(xDiff * xDiff)

o = open('square.out', 'w+')
o.write(answer + '\n')
o.close()