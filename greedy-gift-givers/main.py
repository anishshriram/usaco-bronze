"""
ID: ashrira1
LANG: PYTHON3
TASK: gift1
"""
f = open('gift.in')
f = f.readlines()

n = []
n = f[0].strip('\n').split(' ')

numPeople = int(n[0])

people = {}

for i in range(1, numPeople + 1):
    people[f[i].strip('\n')] = 0

for i in range(numPeople + 1, len(f)):

    if (f[i].strip('\n') not in people):
        num1 = f[i].strip('\n').split(' ')

        if (int(num1[1]) != 0):

            moneyMod = int(num1[0]) % int(num1[1])
            moneySplit = int(int(num1[0]) / int(num1[1]))

            people[f[i - 1].strip('\n')] += moneyMod

            people[f[i - 1].strip('\n')] -= int(num1[0])

            for j in range(i + 1, i + int(num1[1]) + 1):
                people[f[j].strip('\n')] += moneySplit

o = open('gift.out', 'w+')

for key in people:
    o.write(key + " " + str(people[key]) + '\n')

o.close()