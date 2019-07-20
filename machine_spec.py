#!/usr/bin/python
# Modules here
import sys
# This is the basic file that will generate information for the creation of the VM.
print ("Enter the machine name.  If name is not important, enter 0")
sysname = input()

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
