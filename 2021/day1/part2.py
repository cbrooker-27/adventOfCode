increasingCount=0
window1=0
window2=0
with open('input.txt') as f: #read input into file 'f'
    lines = f.read().splitlines() # split lines from file 'f' into 'lines'
    for x in range(len(lines)-3): # use x to iterate through lines
        window1 = int(lines[x])+int(lines[x+1])+int(lines[x+2])
        window2 = int(lines[x+1])+int(lines[x+2])+int(lines[x+3])
        if window2>window1:
            increasingCount = increasingCount+1
            print("when line is {} next sum is greater".format(x))
print("{} increasing counts found".format(increasingCount))