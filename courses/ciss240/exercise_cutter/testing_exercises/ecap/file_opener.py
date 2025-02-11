#The file is opened in read mode
file = open("example.txt", "r")

#The contents of the file are read
contents = file.read()
print("read contents =", contents)

# The current line number is fetched
line_number = contents.count("\n") + 1

# The file is closed
file.close()

# The current line number is printed
print("Current line number:", line_number)
