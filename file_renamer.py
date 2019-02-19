import os


def rename_files():
    path = 'C:\\Users\\marti\\Desktop\\AI\\Secret Message\\files'
    os.chdir(path) # changing to the directory
    file_list = os.listdir()
    print(file_list)

    for filename in file_list:
        print(filename)
        os.rename(os.path.join(path, filename), os.path.join(path, filename.lstrip("0123456789")))
