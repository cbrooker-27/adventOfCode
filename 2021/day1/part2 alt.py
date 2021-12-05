increasingCount=0
with open('input.txt') as f: #read input into file 'f'
    lines = f.read().splitlines() # split lines from file 'f' into 'lines'
    for x in range(len(lines)-3): # use x to iterate through lines
        #since only the first and last numbers are different (the 2 in the middle are shared), we can just compare the two numbers
        if int(lines[x+3])>int(lines[x]):
            increasingCount = increasingCount+1
            print("when line is {} next sum is greater".format(x))
print("{} increasing counts found".format(increasingCount))