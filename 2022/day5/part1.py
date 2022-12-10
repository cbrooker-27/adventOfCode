stacks={
    1:["F","C","J","P","H","T","W"],
    2:["G","R","V","F","Z","J","B","H"],
    3:["H","P","T","R"],
    4:["Z","S","N","P","H","T"],
    5:["N",'V','F','Z','H','J','C','D'],
    6:['P','M','G','F','W','D','Z'],
    7:['M','V','Z','W','S','J','D','P'],
    8:['N','D','S'],
    9:['D','Z','S','F','M']
}
with open('input.txt') as f: #read input into file 'f'
    lines = f.read().splitlines() # split lines from file 'f' into 'lines'
    for x in range(len(lines)): # use x to iterate through lines
        tokens=lines[x].split()# Split into tokens... range=tok[0], letter=tok[1], pwd=tok[2]
        loopCtr=tokens[1]
        fromStack=tokens[3]
        toStack=tokens[5]
        #pop/push 1 at a time
        for y in range(int(loopCtr)):
            temp=stacks[int(fromStack)].pop()
            stacks[int(toStack)].append(temp)
    #print answer (last [aka top] item on stack)       
    for x in range(len(stacks)):
        print(stacks[x+1][len(stacks[x+1])-1])