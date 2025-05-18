def writeToFile(filename, text):
    with open(filename, 'w') as file:
        file.write(text)

def appendToFile(filename, text):
    with open(filename, 'a') as file:
        file.write(text)

def readFromFile(filename):
    with open(filename, 'r') as file:
        return file.read()