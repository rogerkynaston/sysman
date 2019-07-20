#!/usr/bin/python
# Modules here
import sys
# This is the basic file that will generate information for the creation of the VM.
print ("Enter the machine name.  If name is not important, enter 0")
sysname = input('Name:')

print ("Enter the OS type")
print ("1. Linux")
print ("2. Windows")
arch = input('Type:')

print ("Enter location:")
print ("1. AWS")
print ("2. Azure")
print ("3. Google")
print ("4. Local")
location = input('Location:')

if arch == '1':
  print ("Choose the type:")
  print ("1. Web Server")
  print ("2. DB Server")
  print ("3. Storage")
  print ("4. Other")
  lintype = input('Linux Type:')
elif arch == '2':
      print ("Choose the type:")
      print ("1. Domain Controller")
      print ("2. Application Server")
      print ("3. Print Server")
      print ("4. File Server")
      print ("5. Other")
      wintype = input ('Windows Type:')
