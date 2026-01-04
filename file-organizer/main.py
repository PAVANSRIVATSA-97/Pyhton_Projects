import os
# files = os.listdir("file-organizer")
# print(files)
# def arrange_file(files, ext):
#     files_with_ext = [file for file in files if file.endswith(ext)]
#     print(files_with_ext)
#     for i, file in enumerate(files_with_ext, start=1):
#         os.rename(file, f"images/my-pic{i}.{ext}")
# arrange_file(files, ".jpg")

dir = input("Enter the name of the directory: ")
files = os.listdir(dir)
print(files)
ext = input("Enter the extension: ")
def arrange_files(files, ext):
        files_with_ext = [file for file in files if file.endswith(ext)]
        print(files_with_ext)
        folder = input("Enter the folder you want to create: ")
        new_dir = os.path.join(dir, folder)
        print(new_dir)
        if not(os.path.exists(folder)):
            os.makedirs(f"{new_dir}", exist_ok=True) # its better to use makedirs than mkdir as it has built in saftey function exist-ok = True that tell the python not to crash if the folder already exists and also creates the whole path given while mkdir creates the lst leaf of the path.
            # exist_ok=True: This prevents Python from crashing if the folder already exists.
        for file in files_with_ext:
            old_path = os.path.join(dir, file)
            new_name = input("Enter the new name of the file: ")
            new_path = os.path.join(new_dir, f"{new_name}{ext}")
            # os.rename(f"{dir}/{file}", f"{dir}/{folder}/{new_name}{ext}") instead of give the path like this, it is better to give it like below.
            os.rename(f"{old_path}", f"{new_path}")

# if __name__ == "__main__":
arrange_files(files, ext)
