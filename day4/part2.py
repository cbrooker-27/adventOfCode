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
            #now check each of these for required values
            print(entry)
            tokens = entry.split()
            invalid = False
            a=1
            for field in tokens:
                pair = field.split(':')
                label = pair[0]
                value = pair[1]
                #print(pair[0]+"---"+pair[1])
                if field.find("byr:")>-1:
                    if int(value)<1920 or int(value)>2002:
                        print('invalid byr')
                        invalid = True
                elif field.find("iyr:")>-1:
                    if int(value)<2010 or int(value)>2020:
                        print('invalid iyr')
                        invalid = True
                elif field.find("eyr:")>-1:
                    if int(value)<2020 or int(value)>2030:
                        print('invalid eyr')
                        invalid = True
                elif field.find("hgt:")>-1:
                    if value.find('cm')>-1:
                        if int(value[0:value.find('cm')])<150 or int(value[0:value.find('cm')])>193 :
                            print('invalid hgt={}'.format(value[0:2]))
                            invalid = True
                    elif value.find('in')>-1:
                        if int(value[0:value.find('in')])<56 or int(value[0:value.find('in')])>76 :
                            print('invalid hgt')
                            invalid = True
                    else:
                        invalid=True  
                        print('invalid hgt')  
                elif field.find("hcl:")>-1:
                    if value[0]!='#' or len(value)!=7:
                        invalid=True
                        print("invalid hcl")
                    else:
                        try:
                            hexVal=int(value[2:6],16)
                        except:
                            print("invalid hex hcl")
                            invalid=True
                elif field.find("ecl:")>-1:
                    if len(value)==3 :
                        if value == "amb" or value == "blu" or value == "brn" or value == "gry" or value == "grn" or value == "hzl" or value =="oth":
                            a=a
                        else:
                            invalid = True
                            print("invalid ecl")
                    else:
                        invalid = True
                        print("invalid ecl")    
                elif field.find("pid:")>-1:
                    if len(value)==9 :
                         try:
                            x=int(value)
                         except:
                            invalid = True
                            print("invalid pid non-number")                          
                    else:
                        print("invalid pid")
                        invalid=True
            if not invalid: 
                validPassports+=1 #increment the count of good passports
    print("validpassports={}".format(validPassports))