with open('input.txt') as f: #read input into file 'f'
    preamb = 25
    numbers = []
    lines = f.read().splitlines() # split lines from file 'f' into 'lines'
    for x,line in enumerate(lines):
        numbers.append(int(line))
    for x in range(preamb,len(numbers)):
        validNumberFound = False
        for y in range(x-preamb,x):
            for z in range(y+1,x):    
                if (numbers[y]+numbers[z]) == numbers[x]:
                    validNumberFound=True
        if validNumberFound == False:
            print(f"Failed to find a valid combo for x={x} number={numbers[x]}")
   # print(acc)