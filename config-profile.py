#!/usr/bin/python
import sys
with open('delivery/src/main/resources/application.yml', 'r') as file:
    filedata = file.read()
filedata = filedata.replace('PROFILE_APPLICATION', str(sys.argv[1]))
with open('delivery/src/main/resources/application.yml', 'w') as file:
    file.write(filedata)
