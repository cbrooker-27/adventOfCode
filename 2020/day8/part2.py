with open('input.txt') as f: #read input into file 'f'
    acc = 0
   
    magicNumber = -1
    realLines = f.read().splitlines() # split lines from file 'f' into 'lines'
    for x in range(len(realLines)) :
        lines = []
        for line in realLines:#copy the whole set over
            lines.append(line)
        iterator = 0
        acc = 0
        #print('{} {}'.format(x,lines[x]))
        if lines[x][:3]=='nop':
            lines[x]=lines[x].replace('nop','jmp')
           # print('changed {}'.format(lines[x]))
        elif lines[x][:3]=='jmp':
            lines[x]=lines[x].replace('jmp',"nop")
        #run the code
        while iterator < len(lines):
            inst=lines[iterator].split()
            #print('{} {} {} {}'.format(x,iterator,inst,len(lines)))
            if inst[0]=='acc':
                lines[iterator]= 'done this one'
                acc += int(inst[1])
                #print(acc)
            elif inst[0]=='jmp': #else we are at a new line, done with this group
                lines[iterator]= 'done this one'
                iterator += int(inst[1])-1
            elif inst[0]=='done':
                print('Loop detected on run {}, acc={}, iter={} {}'.format(x,acc,iterator,inst))
                iterator = 10000
                
            iterator += 1
            if iterator==len(lines):
                print("found it x={},acc={}".format(x,acc))
       # print (lines)
        #print(realLines)