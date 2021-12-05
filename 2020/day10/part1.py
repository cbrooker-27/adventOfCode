# A function that returns the length of the value:
def stringToInt(e):
  return int(e)

with open('input.txt') as f: #read input into file 'f'
    lines = f.read().splitlines() # split lines from file 'f' into 'lines'
    lines.sort(key=stringToInt)
    upBy1=1 #account for the first jump (yeah, i don't know its one all the time ;-P)
    upBy3=1 #my adapter always creates a 3 volt diff
    for x,line in enumerate(lines):
        if x>0:
            if int(lines[x-1])==int(line)-1:
                upBy1+=1
                print(f"{line} upby1" )
            elif int(lines[x-1])==int(line)-3:
                upBy3+=1
                print(f"{line} upby3" )
            else:
                print("Uhoh")
    print(f"upby1={upBy1} upby3={upBy3} product={upBy1*upBy3}")
