scoregrid ={'A':
                {'X': 3,
                'Y':4,
                'Z':8}
           ,'B':
                {'X':1,
                'Y':5,
                'Z':9}
           ,'C':
                {'X':2,
                'Y':6,
                'Z':7}
}
totalScore=0
with open('input.txt') as f: #read input into file 'f'
    lines = f.read().splitlines() # split lines from file 'f' into 'lines'
    for x in range(len(lines)): # use x to iterate through lines
        theirMove=lines[x][0]
        myMove=lines[x][2]
        totalScore=totalScore+scoregrid[theirMove][myMove]
print('total score =',totalScore)
