f = open('input.txt')
x = []
z = 0
for i in f:
    i = int(i)
    x.append(i)
for m in x:
    for a in x:
        for n in x:
            if x[z] + n == 2020:
                print('Yes', x[z], n)
                c = x[z]*n
                print(c)
            else:
                continue
        break
    z += 1


