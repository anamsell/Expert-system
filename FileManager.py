import Display


def get_content_of_file_named(file_name):
    try:
        fileDescriptor = open(file_name, "r")
        content = fileDescriptor.readlines()
        fileDescriptor.close()
        return content
    except IOError:
        Display.error("No such file named " + file_name)
