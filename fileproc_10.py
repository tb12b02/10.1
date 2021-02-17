import os
import sys

filePath = '/users/ssher/python_work/'
fileName = 'fileproc_10.txt'
def main():

    directory = input("Enter the directory where you want to save the file to: ")
    filename = input("Enter the filename: ")
    name = input("Enter your name: ")
    address = input("Enter your address: ")
    phone_number = input("Enter your phone number: ")

#now need to look for os directory, then create and open file and write it

    if os.path.isdir(directory):
        # 'champions.txt')
        writeFile = open(os.path.append(sys.argv[0]),(directory,filename),'w')
        writeFile.write(name +','+ address +','+ phone_number +'\n')

#must remember to close the file!
        writeFile.close()
        print("File contents:")

#go back and read the file to see if it stored correctly
        readFile = open(os.path.append(sys.argv[0])(directory,filename),'r')
        for line in readFile:
            print(line)
        readFile.close()

    else:
        print("I am sorry.  That directory does not exist.")

main()