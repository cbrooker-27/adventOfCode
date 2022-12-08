scoregrid ={'A':
                {'X': 4,
                'Y':8,
                'Z':3}
           ,'B':
                {'X':1,
                'Y':5,
                'Z':9}
           ,'C':
                {'X':7,
                'Y':2,
                'Z':6}
}
totalScore=0
with open('input.txt') as f: #read input into file 'f'
    lines = f.read().splitlines() # split lines from file 'f' into 'lines'
    for x in range(len(lines)): # use x to iterate through lines
        theirMove=lines[x][0]
        myMove=lines[x][2]
        totalScore=totalScore+scoregrid[theirMove][myMove]
print('total score =',totalScore)
