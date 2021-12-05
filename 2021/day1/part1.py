increasingCount=0
with open('input.txt') as f: #read input into file 'f'
    lines = f.read().splitlines() # split lines from file 'f' into 'lines'
    for x in range(len(lines)-1): # use x to iterate through lines
        if int(lines[x+1])>int(lines[x]):
            increasingCount = increasingCount+1
            print("when line {} is greater than line {}".format(x+1,x))
print("{} increasing counts found".format(increasingCount))