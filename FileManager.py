import Display


def get_content_of_file_named(file_name):
    try:
        file_descriptor = open(file_name, "r")
        content = file_descriptor.readlines()
        file_descriptor.close()
        return content
    except IOError:
        Display.error("No such file named " + file_name)
