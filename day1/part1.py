#python

with open('input.txt') as f:
    lines = f.read().splitlines()
    for x in range(len(lines)):
        for y in range(x+1,len(lines)):
            sum = int(lines[x])+int(lines[y])
            if sum == 2020 :
                product = int(lines[x])*int(lines[y])
                print("x={} y={} {}+{}={} and product = {}".format(x,y,lines[x],lines[y],sum,product))