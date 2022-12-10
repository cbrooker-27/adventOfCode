priority="0abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ"
totalPriority=0
counter=0
group=["","",""]
with open('input.txt') as f: #read input into file 'f'
    lines = f.read().splitlines() # split lines from file 'f' into 'lines'
    for x in range(len(lines)): # use x to iterate through lines
        #get 3 lines
        group[counter]=lines[x]
        counter=counter+1
        if (counter==3):
          counter=0
          found=0
          #check for a character from the first group that is in the others
          for pkg in group[0]:
            if ((group[1].find(pkg)>-1) and (group[2].find(pkg)>-1) and found==0):
                 found=1
                # add up total priority
                 totalPriority=totalPriority+priority.index(pkg)
print('total priority =',totalPriority)
