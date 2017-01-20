import os
os.system('clear')

def rename_files():
    #get file names
    file_list = os.listdir(r"/Users/user/Desktop/prank")
    print(file_list)

    #rename file
    saved_path = os.getcwd()
    print("Current word directory is "+saved_path)
    os.chdir(r"/Users/user/Desktop/prank")
    for file_name in file_list:
        os.rename(file_name, file_name.translate(None,"0123456789"))

rename_files()

