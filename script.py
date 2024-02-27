import os

def search_files(extension):
    found_files = []
    for root, dirs, files in os.walk(os.getcwd()):
        for file in files:
            if file.lower().endswith(extension.lower()):
                found_files.append(file)
    return found_files
