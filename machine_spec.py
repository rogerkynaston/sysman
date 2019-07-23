#!/usr/bin/python
# Here we will just gather the requirements.  Other parts will talk to Terraform and Ansible and whatever.
# Modules here
import sys
#import python_terraform

# define functions here
def errfunc(errstring, exitno):
    # some code to exit (or not) if there is a problem.  Takes string and exit code
    # Allows for both non fatal exit and a fatal. For now, at least, if the program terminates it signals a
    # zero exit code.
    if exitno != 0:
      print ("Error:", errstring)
      sys.exit(0)
    else:
      print ("Error:", errstring)
      return

def systemname():
    # This is the basic file that will generate information for the creation of the VM.
    global sysname
    print ("Enter the machine name.  If name is not important, leave blank")
    sysname = input('Name:')
    return sysname

def ostype():
    # We get overall OS type here
    global arch
    print ("Enter the OS type")
    print ("1. Linux")
    print ("2. Windows")
    arch = input('Type:')
    if arch < '1' or arch > '2':
        errfunc('Architecture out of range', 0)
        ostype()
    else:
        return arch

def winservertype():
    # This will set the type of Windows server we are building
    global wintype
    print ("Choose the type of Windows server:")
    print ("1. Domain Controller")
    print ("2. Application Server")
    print ("3. Print Server")
    print ("4. File Server")
    print ("5. Other")
    wintype = input ('Windows Type:')
    if wintype < '1' or wintype > '5':
        errfunc('Server Type out of range', 0)
        winservertype()
    else:
        return wintype

def linservertype():
    # This will set the type of linux server we are building
    global lintype
    print ("Choose the type:")
    print ("1. Web Server")
    print ("2. DB Server")
    print ("3. Storage")
    print ("4. Other")
    lintype = input('Linux Type:')
    if lintype < '1' or lintype > '4':
        errfunc('Linux Server type out of range', 0)
        linservertype()
    else:
        return lintype

def locationfunc():
    # Obvious really. Where are we putting the server
    global location
    print ("Enter location:")
    print ("1. AWS")
    print ("2. Azure")
    print ("3. Google")
    print ("4. Local")
    location = input('Location:')
    if location < '1' or location > '4':
        errfunc('Location out of range', 0)
        locationfunc()
    else:
        return location

def create_terrfile():
    # This will create the .tf file ready for terraform to create the machine.
    filename = sysname + '.txt'
    filehandle = open(filename, "w")
    # Now we create the tf format and write to the file ready for execution


# now do some actual work
systemname()
locationfunc()
ostype()
if arch == '1':
    linservertype()
elif arch == '2':
    winservertype()

    

if sysname:
   print ("You have chosen to create a machine that is called", sysname)
else:
    print ("You have chosen to set machine name to default")

if arch == '1':
    print ("The architecture is Linux")
    if lintype == '1':
        print ("This will be a web server")
    elif lintype == '2':
        print ("This will be a DB server")
    elif lintype == '3':
        print ("This will be a storage server")
    else:
        print ("This will be a generic linux server ")
elif arch == '2':
    print ("The architecture is Windows")
    if wintype == '1':
        print ("This will be a Domain Controller")
    elif wintype == '2':
        print ("This will be an application server")
    elif wintype == '3':
        print ("This will be a print server")
    elif wintype == '4':
        print ("This will be a file server")
    else:
        print ("This will be a generic Windows server")

elif arch == '2':
    print ("The architecture is Windows")
else:
    print ("Architecture not set correctly")

