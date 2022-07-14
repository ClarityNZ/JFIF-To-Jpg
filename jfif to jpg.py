from os import listdir, curdir, rename
files = listdir(curdir)
for file in files:
    if '.jfif' in file:
        try:
            newfile = file.replace('.jfif', '.jpg')
            rename(file, newfile)
            continue
        except:
            newfile = file.replace('.jfif', '_dupe.jpg')
            rename(file, newfile)
            continue
    elif '.jpg_large' in file:
        try:
            newfile = file.replace('.jpg_large','.jpg')
            rename(file, newfile)
            continue
        except:
            newfile = file.replace('.jpg_large','_dupe.jpg')
            rename(file, newfile)
            continue
        

input("Process completed, press enter to close")