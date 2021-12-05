with open('input.txt') as f: #read input into file 'f'
    passports=[]
    lines = f.read().splitlines() # split lines from file 'f' into 'lines'
    curPass = "" #prime temp variable
    for row in range(len(lines)): # use row to iterate through lines
        if lines[row] != "" : #if it is not a blank line, add to the current passport
            curPass += lines[row] + " "
        else: #else we are at a new line, done with this passport
            passports.append(curPass)
            curPass = "" #clear it out for the next one
    passports.append(curPass)
    
    validPassports = 0 # start with 0
    for entry in passports: #for each passport
        #if it has something for each of the required fields
        if entry.find('byr:')>=0 and entry.find('iyr:')>=0 and entry.find('eyr:')>=0 and entry.find('hgt:')>=0 and entry.find('hcl:')>=0 and entry.find('ecl:')>=0 and entry.find('pid:')>=0 :
            validPassports+=1 #increment the count of good passports
    print(validPassports)