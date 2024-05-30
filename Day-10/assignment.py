import os

folder_paths = input("please enter your folder names with a space in between: ").split()


for folder_path in folder_paths:
    files = os.listdir(folder_path)
    print("***** Here are the files in this folder path: ", folder_path, " *****")
    
    for file in files:
        print(file)
