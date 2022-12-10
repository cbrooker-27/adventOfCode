count=0
with open('input.txt') as f: #read input into file 'f'
    lines = f.read().splitlines() # split lines from file 'f' into 'lines'
    for x in range(len(lines)): # use x to iterate through lines
        elf=lines[x].split(',')
        range1=elf[0].split('-')
        range2=elf[1].split('-')
        #if first elf is contained by the 2nd
        if(((int(range1[0])>=int(range2[0])) and
           (int(range1[1])<=int(range2[1]))) or
        #or 2nd elf is contained by the 1st
          ((int(range2[0])>=int(range1[0])) and
           (int(range2[1])<=int(range1[1])))):
            
            count+=1
    print("count=",count)