#!/usr/local/bin/python
# This is the basic file that will generate information for the creation of the VM.
sysname = input('Enter the machine name. If machine name is not specific enter 0:')

print ("Enter the Machine type")
print ("1. Linux")
print ("2. Windows")
arch = input('Type:')

print ("Enter location:")
print ("1. AWS")
print ("2. Azure")
print ("3. Google")
print ("4. Local")
location = input('location')

print ("Testing:", sysname)
print ("Testing:", location)
print ("Testing:", arch)
