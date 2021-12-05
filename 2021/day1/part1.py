with open('input.txt') as f: #read input into file 'f'
    lines = f.read().splitlines() # split lines from file 'f' into 'lines'
    for x in range(len(lines)): # use x to iterate through lines
        for y in range(x+1,len(lines)): # use y to also iterate through lines
            sum = int(lines[x])+int(lines[y]) # figure out the sum of the numbers on line x and y
            if sum == 2020 : # if the sum is 2020
                product = int(lines[x])*int(lines[y]) #find the product of the magic numbers
                print("x={} y={} {}+{}={} and product = {}".format(x,y,lines[x],lines[y],sum,product)) #print the values of x and y, sum and product
