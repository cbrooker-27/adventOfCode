with open('input.txt') as f: #read input into file 'f'
    lines = f.read().splitlines() # split lines from file 'f' into 'lines'
    for x in range(len(lines)): # use x to iterate through lines
        for y in range(x+1,len(lines)): # use y to also iterate through lines
            for z in range(y+1,len(lines)): # use y to also iterate through lines
                sum = int(lines[x])+int(lines[y])+int(lines[z]) # figure out the sum of the numbers on line x and y and z
                if sum == 2020 : # if the sum is 2020
                    product = int(lines[x])*int(lines[y])*int(lines[z]) #find the product of the magic numbers
                    print("x={} y={} z={} {}+{}+{}={} and product = {}".format(x,y,z,lines[x],lines[y],lines[z],sum,product)) #print the values of x y z, sum and product
