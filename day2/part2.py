with open('input.txt') as f: #read input into file 'f'
    lines = f.read().splitlines() # split lines from file 'f' into 'lines'
    goodPasswords = 0
    for x in range(len(lines)): # use x to iterate through lines
        tokens=lines[x].split() # Split into tokens... range=tok[0], letter=tok[1], pwd=tok[2]
        letterRange = tokens[0].split('-') # Split letter range into two
        letter = tokens[1][0:1] #separate the letter from the ":"
        #if the letter is in one place or the other, but not both, it is good
        if (letter == tokens[2][int(letterRange[0])-1] or letter == tokens[2][int(letterRange[1])-1]) and not ( (letter == tokens[2][int(letterRange[0])-1]) and (letter == tokens[2][int(letterRange[1])-1])) : 
                goodPasswords += 1 # increment the counter    
    print(goodPasswords) #print good password count