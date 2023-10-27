from os import listdir, curdir, rename
files = listdir(curdir)
renamed_files = 0
duped_files = 0

for file in files:
    if '.jfif' in file:
        try:
            newfile = file.replace('.jfif', '.jpg')
            rename(file, newfile)
            renamed_files += 1
            continue
        except:
            newfile = file.replace('.jfif', '_dupe.jpg')
            rename(file, newfile)
            duped_files += 1
            continue
    elif '.jpg_large' in file:
        try:
            newfile = file.replace('.jpg_large','.jpg')
            rename(file, newfile)
            renamed_files +=1
            continue
        except:
            newfile = file.replace('.jpg_large','_dupe.jpg')
            rename(file, newfile)
            duped_files += 1
            continue
        

input("Successfully renamed {renamed_files} file/s and duped {duped_files}\npress enter to close.".format(renamed_files = renamed_files, duped_files = duped_files))
