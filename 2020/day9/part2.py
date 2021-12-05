with open('input.txt') as f: #read input into file 'f'
    preamb = 25
    numbers = []
    weaknessSum=0
    weaknessIndex = 0
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
            weaknessSum = numbers[x]
            weaknessIndex = x
    #go back and look for any sequence of numbers that adds up to the weaknessSum
    for x in range(weaknessIndex-1):
        tempSum = 0
        iterator=x
        while tempSum<weaknessSum and iterator<weaknessIndex-1:
            tempSum+=numbers[iterator]
            if tempSum == weaknessSum:
                #find the min and max of the sequence and add them together
                myMin = numbers[iterator]
                myMax = 0
                for y in range(x,iterator):
                    if numbers[y]<myMin:
                        myMin = numbers[y] 
                    if numbers[y]>myMax:
                        myMax = numbers[y]
                print(f"my Min={myMin} my Max={myMax} sum = {myMin+myMax}")
            iterator+=1
   