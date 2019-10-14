class FileManager:


    @staticmethod
    def getContentOfFileNamed(fileName):
        fileDescriptor = open(fileName, "r")
        content = fileDescriptor.readline()
        fileDescriptor.close()

        return content