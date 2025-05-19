def printASCIITable():
    for i in range(32, 127):
        print(i, chr(i))
        #Prints the # and their character based on unicode value
printASCIITable()