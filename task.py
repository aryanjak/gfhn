a = open("file.txt")
lines = a.readlines()
count = 0
for li in lines:
    words = li.split()
    count = count+len(words)
   
print(count)