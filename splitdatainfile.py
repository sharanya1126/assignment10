with open("sample.txt") as f:
   data=f.readlines()
   for line in data:
       word=line.split("")
       print(word)
