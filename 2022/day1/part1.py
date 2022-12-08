calories=[0]
currentElf=0
with open('input.txt') as f: #read input into file 'f'
    lines = f.read().splitlines() # split lines from file 'f' into 'lines'
    for x in range(len(lines)-1): # use x to iterate through lines
        if (lines[x]==""):
            currentElf=currentElf+1
            calories.append(0) # add a new elf with 0 calories  
        else:
            calories[currentElf]=calories[currentElf]+int(lines[x])
print('max cals found =',max(calories))
