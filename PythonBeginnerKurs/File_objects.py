# Files
# how to open files in a way which is not recommend

f = open("test.txt", "r")
# needs to specify if want to read, write, append or read&write
    # read a file is r
    # write into a file is w
    # appending in a file is a (will append to the end of the file)
    # read&write is r+
    # create a file by using x

print(f.name)
# 1)
# .name will print the name of the file & NOT what's inside
# .mode will print the whether file is open for reading, writing, appen... etc.
# .read() will return whole text / if you want to specify put an index into brackets .read(5)
# .readline() will only read one line (starting at the top) if you print multiple times then
#   it will read the second, third, etc.
# .readlines() will return every line in a list
#   can put a hint into brackets in order to give only a certain amound of characters back

# if we open a file we need to explicit close it !!!
f.close()

# in order to be safe use a context manager to work with files in Python
# context manager will always close file for us if we work with one - very cool
# f is an object variable and we have access to it but its still closed
# that's why we have to work within the context manager
with open ("test.txt", "r") as f:
    f_contents = f.read() # can add functions now from 1)
    print(f_contents)

# if you have a blank line in console just print it like this: print(f_contents, end=" "
#   end=" " will remove blank line and always print next line if previous line ends

# you can iterate through the file by using a for loop, which makes it more efficent
with open ("test.txt", "r") as f:
    for line in f: # line is just a variable name, could be named as anything
        print(f_contents, end=" ")

# .read(hint) specification how many characters to read
with open ("test.txt", "r") as f:
    f_contents = f.read(100) # reads 100 characters and then stops
    f_contents = f.read(100) # can repeat it multiple times until file has no more characters

# more control over what's is going to be read
with open ("test.txt", "r") as f:
    size_to_read = 100

    f_contents = f.read(size_to_read) # put into variable f_contents the first 100 characters and read it

    while len(f_contents) > 0:
        print(f_contents, end=" ")
        f_contents = f.read(size_to_read) # very important line here -> or else infinit loop
        # after the first 100 characters we tell the loop the take the next chunk of 100 characters
        # if the variable has 0 characters (empty string) then the while loop will end BC of set conditions

with open ("test.txt", "r") as f:
    size_to_read = 10

    f_contents = f.read(size_to_read)
    print(f.tell()) # will tell us the position in the file where we are currently in (in this case its 10)

# How to go back to the beginning of the file?
# use .seek()

with open ("test.txt", "r") as f:
    size_to_read = 10

    f_contents = f.read(size_to_read)   # will print first 10 characters
    print(f_contents)
    f.seek(0)                           # will go back to position 0
    f_contents = f.read(size_to_read)   # will print the first 10 characters of the file again
    print(f_contents)

# HOW TO WRITE INTO FILES
# In case the file doesn't exist already it will create a new file automatically
with open ("test.txt", "w") as f:
    f.write("Test") # will write "Test" into the file
    # quick fact
    f.seek(0)       # goes back to index 0
    f.write("R")    # would only over write the letter T so in the file it will be "Rest" now
                    # or.. when use a word like "Sea" then in the file will be "Seat"

# How to pick up lines from one file and write them into the other?

with open ("test.txt", "r") as rf: # "r" only in read mode , named variable rf for read file
    with open("test_copy.txt", "w") as wf: # "w" in write mode, named wf for write file
        for line in rf:     # for each line in our original line read it
            wf.write(line)  # and write it into the new file

# in Order to work with pictures we need to work with binary mode
with open ("test.jpg", "rb") as rf: # added b after r for read in binary mode
    with open("test_copy.jpg", "wb") as wf: # added b after w for write in binary mode
        for line in rf:
            wf.write(line) # will print each line from the picture and writes it into the new .jpg file
                           # out come will be a copied .jpg file


with open ("test.jpg", "rb") as rf:
    with open("test_copy.jpg", "wb") as wf:
        chunk_size = 4096 # the amount of data we want the program to read
        rf_chunk = rf.read(chunk_size) # put in 4096 into variable rf_chunk and read it
        while len(rf_chunk) > 0:
            wf.write(rf_chunk) # take rf_chunk and write it into new file
            rf_chunk = rf.read(chunk_size) # to avoid infinite loop take new chunk