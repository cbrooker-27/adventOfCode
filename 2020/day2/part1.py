with open('input.txt') as f: #read input into file 'f'
    lines = f.read().splitlines() # split lines from file 'f' into 'lines'
    goodPasswords = 0
    for x in range(len(lines)): # use x to iterate through lines
        tokens=lines[x].split()# Split into tokens... range=tok[0], letter=tok[1], pwd=tok[2]
        letterRange = tokens[0].split('-')  # Split letter range into two
        instances = tokens[2].count(tokens[1][0:1]) # count the instances of the given letter in the password
        if (instances >= int(letterRange[0])) and (instances <= int(letterRange[1])):  # if the count is in range
            goodPasswords += 1 # increment the counter
    print(goodPasswords) #print the counter