import Display


def getContentOfFileNamed(fileName):
    try:
        fileDescriptor = open(fileName, "r")
        content = fileDescriptor.readlines()
        fileDescriptor.close()
        return content
    except IOError:
        Display.error("No such file named " + fileName)
