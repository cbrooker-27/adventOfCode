with open('input.txt') as f: #read input into file 'f'
    lines = f.read().splitlines() # split lines from file 'f' into 'lines'
    treesHit = [0,0,0,0,0] #save each run
    slope=[[1,1],[1,3],[1,5],[1,7],[2,1]] #programatic slopes
    product = 1 # seed the product
    for index, thisSlope in enumerate(slope): #for each requested slope
        col = 0 #start fresh at the left
        for row in range(0,len(lines),thisSlope[0]): # use row to iterate through lines , start at top, iterate down by slope var
            if lines[row][col%len(lines[row])] == '#' : # if we hit a tree
                treesHit[index]+=1 # bump counter
            col+=thisSlope[1] # move right as instructed
        product*=treesHit[index] # Now that we're done with this trip, multiply against previous product
    print(product) #print the answer