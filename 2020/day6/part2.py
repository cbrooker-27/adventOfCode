with open('input.txt') as f: #read input into file 'f'
    groups=[]
    lines = f.read().splitlines() # split lines from file 'f' into 'lines'
    currGroup = " " #prime temp variable
    for row in range(len(lines)): # use row to iterate through lines
        if lines[row] != "" : #if it is not a blank line, add to the current group
            #currGroup += lines[row] + ""
            if currGroup==" ": #if this is the first member of a group
                currGroup = lines[row] #prime currGroup with all the first persons answers
            else:
                newCurrGroup = ''
                for letter in lines[row]:
                    if currGroup.find(letter)>-1:
                        newCurrGroup += letter
                currGroup = newCurrGroup
        else: #else we are at a new line, done with this group
            groups.append(currGroup)
            currGroup = " " #clear it out for the next one
    groups.append(currGroup)
    
    sumOfGroups = 0 # start with 0
    for entry in groups: #for each group
        print("{}.{}".format(len(entry),entry))
        #uniqueAnswer = ''.join(set(entry)) #strip to unique letters
        sumOfGroups+=len(entry) #add count of unique letters
    print(sumOfGroups)