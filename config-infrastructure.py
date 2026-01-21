#!/usr/bin/python
import sys
with open('infrastructure/src/main/resources/application.properties', 'r') as file:
    filedata = file.read()

filedata = filedata.replace('DATABASE_URL', str(sys.argv[1]))
filedata = filedata.replace('DATABASE_USER', str(sys.argv[2]))
filedata = filedata.replace('DATABASE_PW', str(sys.argv[3]))
filedata = filedata.replace('AWS_REGION', str(sys.argv[4]))
filedata = filedata.replace('AWS_ACCOUNT_ID', str(sys.argv[5]))
filedata = filedata.replace('PRESCRIPTION_BEARER_TOKEN', str(sys.argv[6]))


with open('infrastructure/src/main/resources/application.properties', 'w') as file:
    file.write(filedata)
