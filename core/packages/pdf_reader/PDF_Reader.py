import os

content = 'CV - Ravindu Rashmika.pdf'

from textract import process

text = process(content)
data = text.split("\n")
# print data
for i in range(0, len(data)):
    if data[i] == "Full Name":
        print "Full Name: ", data[i + 2]
    if data[i] == "Contact Nos.":
        print "Contact Nos.: ", data[i + 2]
    if data[i] == "Email":
        print "Email: ", data[i + 2]
    if data[i] == "NIC No":
        print "NIC No: ", data[i + 2]
    if data[i] == "Nationality":
        print "Nationality: ", data[i + 2]
    if data[i] == "Gender":
        print "Gender: ", data[i + 2]
    if data[i] == "Date of Birth":
        print "Date of Birth: ", data[i + 2]
    if data[i] == "Marital Status":
        print "Marital Status: ", data[i + 2]
    if data[i] == "Spoken Languages":
        print "Spoken Languages: ", data[i + 2]