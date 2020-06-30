try:
    f=open("sample.txt")
    data=f.read()
    print(data)
except:
    print("file can't be opened")
    exit()
