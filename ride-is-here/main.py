"""
ID: ashrira1
LANG: PYTHON3
TASK: ride
"""

f = open('ride.in')
f = f.readlines()

answer = "STAY"

a = []
b = []

for i in range(len(f)):
  if i % 2 == 0:
    a.append(f[i].strip('\n').split(' '))
  else:
    b.append(f[i].strip('\n').split(' '))

cometName = a[0][0]
groupName = b[0][0]

cValue = 1
for char in cometName:
  number = ord(char) - 64
  cValue *= number

gValue = 1
for char in groupName:
  number = ord(char) - 64
  gValue *= number

c47 = cValue % 47
g47 = gValue % 47

if (c47 == g47):
  answer = "GO"

o = open('ride.out', 'w+')
o.write(answer + '\n')
o.close()