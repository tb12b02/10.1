import os

def main():

    directory = input("Please enter the directory where you would like the file saved: ")
    filename = input("Enter the filename: ")
    name = input("Enter your name: ")
    address = input("Enter your address: ")
    phone_number = input("Enter your phone number: ")

#now need to look for os directory, then create and open file and write it

    if os.path.isdir(directory):
        writeFile = open(os.path.join(directory,filename),'w')
        writeFile.write(name +' , '+ address +' , '+ phone_number +'\n')

#must remember to close the file!
        writeFile.close()

        print("File contents are:")

#go back and read the file to see if it stored correctly
        readFile = open(os.path.join(directory,filename),'r')
        for line in readFile:
            print(line)
        readFile.close()

    else:
        print("I am sorry.  That directory does not exist.")

main()