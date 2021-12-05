with open('input.txt') as f: #read input into file 'f'
    acc = 0
    iterator = 0
    lines = f.read().splitlines() # split lines from file 'f' into 'lines'
    while iterator < len(lines):
        inst=lines[iterator].split()
        if inst[0]=='acc':
            lines[iterator]= 'done this one'
            acc += int(inst[1])
            print(acc)
        elif inst[0]=='jmp': #else we are at a new line, done with this group
            lines[iterator]= 'done this one'
            iterator += int(inst[1])-1
        elif inst[0]=='done':
            iterator = 10000
            print(acc)
        iterator += 1    
   # print(acc)