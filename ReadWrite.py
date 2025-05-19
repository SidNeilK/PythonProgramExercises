def writeToFile(filename, text):
    with open(filename, 'w') as file:
        file.write(text)
        #Creates new file and writes text
def appendToFile(filename, text):
    with open(filename, 'a') as file:
        file.write(text)
        #Adds content end of the file
def readFromFile(filename):
    with open(filename, 'r') as file:
        return file.read()
        #Opens the file and returns the content

writeToFile('greet.txt', 'Hello!\n')
appendToFile('greet.txt', 'Goodbye!\n')

assert readFromFile('greet.txt') == 'Hello!\nGoodbye!\n'

