import zipfile,os


for root, dirs, files in os.walk("."):
    print (files)
    for file in files:
        if file.endswith(".jar"):
            with zipfile.ZipFile(os.path.join(root, file)) as z:
 #               print("extracting : " + os.path.join(root, file))
                z.extractall(root)

