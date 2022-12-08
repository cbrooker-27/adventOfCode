calories=[0]
currentElf=0
maxCals=0
maxCals2=0
maxCals3=0
with open('input.txt') as f: #read input into file 'f'
    lines = f.read().splitlines() # split lines from file 'f' into 'lines'
    for x in range(len(lines)-1): # use x to iterate through lines
        if (lines[x]==""):
            currentElf=currentElf+1
            calories.append(0)# add a new elf with 0 calories
            
        else:
            calories[currentElf]=calories[currentElf]+int(lines[x])
maxCals =max(calories)
calories.remove(max(calories))
maxCals2 =max(calories)
calories.remove(max(calories))
maxCals3=max(calories)
calories.remove(max(calories))
print('top 3 total is ',maxCals+maxCals2+maxCals3)

