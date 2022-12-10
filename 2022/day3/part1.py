priority="0abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ"
totalPriority=0
with open('input.txt') as f: #read input into file 'f'
    lines = f.read().splitlines() # split lines from file 'f' into 'lines'
    for x in range(len(lines)): # use x to iterate through lines
        #cut line in half
        half1=lines[x][0:int(len(lines[x])/2)]
        half2=lines[x][int(len(lines[x])/2):int(len(lines[x]))]
        found=0
        #find dup letter
        for pkg in half1:
          if ((half2.find(pkg)>-1) and (found==0)):
               found=1
               #add up total priority
               totalPriority=totalPriority+priority.index(pkg)
print('total priority =',totalPriority)
