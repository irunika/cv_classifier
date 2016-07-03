import config
from core.dbmgt.usermgt.user import User
# content = 'CV - Ravindu Rashmika.pdf'

from textract import process


def CV_reader(fileName):
    global FullName, ContactNos, Email, NICNo, Nationality, Gender, DateofBirth, MaritalStatus, SpokenLanguages
    file = config.PathToUpload + fileName
    text = process(file)
    data = text.split("\n")

    try:
        for i in range(0, len(data)):
            if data[i] == "Full Name":
                FullName = data[i + 2]
            if data[i] == "Contact Nos.":
                ContactNos = data[i + 2]
            if data[i] == "Email":
                Email = data[i + 2]
            if data[i] == "NIC No":
                NICNo = data[i + 2]
            if data[i] == "Nationality":
                Nationality = data[i + 2]
            if data[i] == "Gender":
                Gender = data[i + 2]
            if data[i] == "Date of Birth":
                DateofBirth = data[i + 2]
            if data[i] == "Marital Status":
                MaritalStatus = data[i + 2]
            if data[i] == "Spoken Languages":
                SpokenLanguages = data[i + 2]
        user = User(FullName, ContactNos, Email, NICNo, Nationality, Gender, DateofBirth, MaritalStatus,
                    SpokenLanguages)
        return user
    except:
        return "Wrong Template"
