
"""
r = open for reading
w = open for writting and truncatingthe file first
x = create a new file and open it for writing
a = open for writting , appending at the endof the file of ot exist
b = binary mode
t = text mode(default)
+ = open a disk file forupdating (reading and writting)
r+ = read,overwrite,notruncate(ptr start)
w+ = read,overwrite,trucate
a+ = append,notruncate(ptr end)


# reading a file
# f.read() read entire file
# f.readline() read one line at a time

f=open("sample.txt","a")
f.write("\n but i am not.")
f.close()

f=open("sample.txt","r")
data=f.read()
print(type(data))
f.close()

f=open("demo.txt","r")
data=f.read()
print(data)
f.close()


# with syntax

with open("sample.txt","r") as f:
        data = f.read()
        print(data)
        
with open("demo.txt","w") as f:    
        f.write("\n new data")    
        
        
# deleting aa file (using the os module)
improt os
os.remove("sample.txt")


# practice

f = open("practice.txt","w")
f.write("\nHi everyone")
f.write("\nwe are learning file i/o")
f.write("\nusing java")
f.write("\ni like programing in java.")

f.close()

"""


with open("practice.txt","r")as f:
    data=f.read()
    
    new_data=data.replace("java","python")
    print(new_data)