file = open("my_file.py")
lines = file.readlines()
print(lines,type(lines))
file.close()


file_read = open("my_file.txt")
lines_read = file_read.read()
print(lines_read)
file_read.close()

str = ("i am very happy to see you and very well")
file_write = open("my_file.txt","w")
file_write.write(str)
file_write.close()

with open("my_file.txt") as f:
    print(f.read())
