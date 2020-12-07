with open('input.txt') as f: #read input into file 'f'
    lines = f.read().splitlines() # split lines from file 'f' into 'lines'
    maxNumber = 0
    minNUmber = 999
    takenSeats = ""
    #F=0, B=1, R=1, L=0
    for line in lines: # use row to iterate through lines
        row=int(line[0:7].replace('F',"0").replace('B','1'),2) #convert row to binary
        col=int(line[7:10].replace('R','1').replace("L","0"),2) #convert col to binary
        seatValue = (row*8)+col #calculate seat number
        if seatValue > maxNumber: # see if it is the new max
            maxNumber = seatValue
        if seatValue < minNUmber:
            minNUmber = seatValue
        takenSeats += " " + str(seatValue)
    for x in range(minNUmber,maxNumber):
        if takenSeats.find(str(x))<0:
            print(x)