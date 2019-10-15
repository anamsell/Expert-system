from Error import Error


class FileManager:


    @staticmethod
    def getContentOfFileNamed(fileName):
        try:
            fileDescriptor = open(fileName, "r")
            content = fileDescriptor.readline()
            fileDescriptor.close()
            return content
        except:
            Error.showError("No such file named " + fileName)
