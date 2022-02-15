import sys
import os



print(sys.version)


def funct(list_var):
    print(list_var)

list_var=[1,2,3,4,5]
funct(list_var)


def createadir(dirname):
    presentwd=os.getcwd()
    if not os.path.isdir(dirname):
        os.mkdir(dirname)
    os.chdir(presentwd+'\\'+dirname)
    if not os.path.isfile("testfile.txt"):
        f = open("testfile.txt","w")
        f.write("He who conquers is the emperor")
        f.close()
        f = open("testfile.txt","r")
        print(f.read())
        f.close()
    else:
        f = open("testfile.txt", "w")
        f.write("He who conquers is the emperor")
        f.close()
        f = open("testfile.txt","r")
        print(f.read())
        f.close()
    os.remove("testfile.txt")    
    os.chdir("..")
    os.getcwd()
    os.rmdir(dirname)

createadir("testdir")