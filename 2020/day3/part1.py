with open('input.txt') as f: #read input into file 'f'
    lines = f.read().splitlines() # split lines from file 'f' into 'lines'
    treesHit = 0 # seed the counter
    col = 0 # start at the left
    for row in range(len(lines)): # use row to iterate through lines
        if lines[row][col%len(lines[row])] == '#' : # if we hit a tree
            treesHit+=1 # bump counter
        col+=3 # move right
    print(treesHit) #print the counter